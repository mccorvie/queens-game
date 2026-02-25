#!/usr/bin/env python3
"""
Fetch puzzle levels from GitHub and convert to puzzles.js format.
Probes level1.ts through level445.ts and extracts colorRegions data.
"""

import urllib.request
import urllib.error
import re
import json
import time
import sys

BASE_URL = "https://raw.githubusercontent.com/abd0-omar/queens-game-linkedin/main/src/utils/levels/level{}.ts"

def fetch_level(num):
    """Fetch a level file and return its content, or None if not found."""
    url = BASE_URL.format(num)
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        print(f"  HTTP error {e.code} for level {num}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  Error fetching level {num}: {e}", file=sys.stderr)
        return None

def parse_level(content, num):
    """Parse the TypeScript file and extract the region grid as numeric indices."""
    # Extract the colorRegions array
    # It's a 2D array of quoted strings like ["A", "B", ...]
    match = re.search(r'colorRegions\s*:\s*\[(.*?)\]\s*,\s*regionColors', content, re.DOTALL)
    if not match:
        # Try alternative pattern
        match = re.search(r'colorRegions\s*:\s*\[(.*?)\]\s*,', content, re.DOTALL)
    if not match:
        print(f"  Could not parse colorRegions for level {num}", file=sys.stderr)
        return None

    raw = match.group(1)

    # Extract each row: find all [...] arrays
    rows_raw = re.findall(r'\[([^\]]+)\]', raw)
    if not rows_raw:
        print(f"  No rows found for level {num}", file=sys.stderr)
        return None

    # Parse letters from each row
    grid = []
    letter_set = set()
    for row_str in rows_raw:
        letters = re.findall(r'"(\w+)"', row_str)
        if not letters:
            letters = re.findall(r"'(\w+)'", row_str)
        grid.append(letters)
        letter_set.update(letters)

    if not grid:
        return None

    size = len(grid)

    # Map letters to numeric indices (in order of first appearance, reading L-R T-B)
    letter_to_idx = {}
    next_idx = 0
    for row in grid:
        for letter in row:
            if letter not in letter_to_idx:
                letter_to_idx[letter] = next_idx
                next_idx += 1

    # Convert to numeric grid
    numeric_grid = []
    for row in grid:
        numeric_grid.append([letter_to_idx[l] for l in row])

    return {
        'number': num,
        'size': size,
        'regions': numeric_grid
    }

def main():
    puzzles = []
    found = 0
    not_found = 0

    for num in range(1, 446):
        sys.stdout.write(f"\rFetching level {num}/445 (found: {found})...")
        sys.stdout.flush()

        content = fetch_level(num)
        if content is None:
            not_found += 1
            continue

        puzzle = parse_level(content, num)
        if puzzle:
            puzzles.append(puzzle)
            found += 1

        # Small delay to be polite
        time.sleep(0.05)

    print(f"\rDone! Found {found} puzzles, {not_found} missing.         ")

    # Sort by puzzle number
    puzzles.sort(key=lambda p: p['number'])

    # Write as puzzles.js format
    output_path = "puzzle-extract.js"
    with open(output_path, 'w') as f:
        f.write("// Extracted from github.com/abd0-omar/queens-game-linkedin\n")
        f.write("// Auto-generated - do not edit manually\n\n")
        f.write("const PUZZLES_EXTRACT = [\n")
        for i, p in enumerate(puzzles):
            f.write("  {\n")
            f.write(f"    number: {p['number']},\n")
            f.write(f"    size: {p['size']},\n")
            f.write("    regions: [\n")
            for j, row in enumerate(p['regions']):
                comma = "," if j < len(p['regions']) - 1 else ""
                f.write(f"      [{','.join(str(x) for x in row)}]{comma}\n")
            f.write("    ]\n")
            comma = "," if i < len(puzzles) - 1 else ""
            f.write(f"  }}{comma}\n")
        f.write("];\n")

    print(f"Saved to {output_path}")

if __name__ == '__main__':
    main()

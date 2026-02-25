# Queens Puzzle

A browser-based implementation of the Queens logic puzzle, inspired by the LinkedIn Queens game.

## How to Play

Place exactly one queen in every **row**, **column**, and **color region** of the grid. No two queens may touch each other — not even diagonally.

Click a cell once to place an **×** mark, click again to place a **♛ queen**, and once more to clear it.

## Features

- Multiple puzzle sizes (7×7 through 12×12 and beyond)
- Timer
- Undo (Ctrl+Z)
- Auto-× — automatically marks off cells that can no longer hold a queen after one is placed
- Randomize — applies a random board symmetry and color permutation so each puzzle feels fresh
- Queen progress bar — shows how many queens are still to be placed

## Files

| File | Description |
|------|-------------|
| `queens` | Main game (open in a browser) |
| `puzzles.js` | Puzzle definitions |
| `editor.html` | Tool for extracting new puzzles from screenshots |
| `fetch-levels.py` | Script for fetching puzzle data |

## Adding Puzzles

Open `editor.html`, paste or drop a screenshot of a Queens board, mark the grid corners, click **Detect Regions**, review and fix the color map, then click **Generate Config**. Paste the output into the `PUZZLES` array in `puzzles.js`.

## Running Locally

No build step required. Serve the directory with any static file server, for example:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080/queens` in your browser.

## Analytics (optional)

If you want Google Analytics, create a `googletag.html` file in the project root containing your Google tag snippet. This file is excluded from the repository via `.gitignore`.

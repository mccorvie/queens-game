
Build me a browser-based game which is a clone of the LinkedIn Queens puzzle.


It should be a single HTML file with no dependencies.  It should be able to read configurations which describe the game board.

The rules of queens:
- There is an n x n grid of squares.  Typical values of n are 7 to 12
- The squares of the grid are color coded into n contiguous regions.  Squares in a region must be joined at edges, not at corners.
- The game is solved when each row and each column and each color region has exactly one Queen
- No two queens can be in the same column. No two queens can be in the same row.  No two queens can be in the same color region.  
- No two queens can be in adjacent squares which touch by an edge or a vertex.  This means that no two queens can be one "King's move" apart.  Note that it is possible for two queens to be on the same diagonal, so long as they are not in adjacent squares.

Here is the game play:
- The player can click on an empty square to add an "X" to that square.  The X has no effect on game play, its just useful for the player who is using logic to rule out squares where there can be a queen
- The player can click on a square with an X to add a queen.  In this way, a double click results in a queen
- The player can click on a square with a queen to clear the square.
- In the case that the player adds a queen in a position which is not allowed (in the same row, column, color as another queen or adjacent to another queen), the board will highlight the queens in red or something to indicate this is illegal.
- There should be an option to toggle on or off "Auto-X".  In the case when Auto X is on, then upon adding a queen, all of the squares in the same row, same column, and same color and squares adjacent to the queen are X'd out.
- if Auto X is on, and a queen is removed, then all the X's added by Auto X from that queen should be removed.  Other X's added by the user, even if they were in the same squares, should not be removed.
- There is a clock which shows how much time has elapsed since the game began
- There is a button to reset the board, which clears all X's and queens and restarts the clock.
- There is an "undo" button which undoes each previous click in turn. Recall that clicking can add an X, Queens or clear a square.
- Holding the mouse and dragging over several squares should be the same as clicking each square to add an X.  Dragging over a square should not promote an X to a queen or clear the square.  X's added by drag-clicking should be undone with the undo button.
- When a winning configuration has been completed, the game should stop the clock and show a congratulatins message

In phase 2 of the project, I would like to create an archive of historical games.  Anticipating this, there should be some system to store a library of configurations which can be loaded in the game.  For now we can just have a single game board.  This game board is a decent place to start:
https://www.archivedqueens.com/



For reference

1) Here is the original game

https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.linkedin.com/games/queens&ved=2ahUKEwji-5209tmSAxXjJDQIHc4aC3kQFnoECBsQAQ&usg=AOvVaw0ZIYT_p1wYxg8QPkfK5iT-

2) Here are two clones of the game which does not require a log in

https://www.playqueensgame.com/puzzles/8x8/1

https://www.archivedqueens.com/ 


3) Here is another description of the rules:

https://www.linkedin.com/help/linkedin/answer/a6269510



Let's start on phase 2

There are a couple of sources for historical gameboards and solutions.  

Are you able to scrape any of these?

https://crossclimbanswer.today/linkedin-queens-answers/646


https://crossclimbanswer.today/linkedin-queens-answers/all-queens-answers


https://tryhardguides.com/linkedin-queens-answer-today/


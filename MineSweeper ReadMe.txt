HW8 ReadMe File
Mike McDonald


######################
Running minesweeper.py
######################

1. Run command "python3 minesweeper.py"
2. The game will prompt for how large a board you would like to play, provide an answer in the form of a digit for the width of the game board you would like. 
3. The game will prompt for how many mines to place - Provide an answer between 0 and the maximum number of tiles on the board (maximum would be the square of the board size response). Difficulty is based upon the number of mines compared to the number of spaces on the board
4. The game board will then be printed to the terminal. Unknown spaces are represented with O's, Flags are P's and Bombs are X's. 
5. Begin game play by providing coordinates for which square to address, and what action to take. The game will prompt for an horizontal (x) coordinate, then a vertical (y) coordinate, then an action for whether to clear (C) the space or flag (F) the space

######################
      Game Rules
######################

1. The objective of the game is to clear the mine field by flagging all bombs, and clearing all non-bomb spaces without clearing a bomb. If a bomb is cleared, the game is over and the player has lost 
2. Unknown spaces are represented with O's, Flags are P's and Bombs are X's. 
3. The cleared spaces will display a number or be blank. The number displayed (or lack of number) will indicate the number of mines in the immediate proximity. For example if 3 of the neighboring cells contain bombs, the cleared cell will have the number 3
4. To begin, select a space to clear. The cleared space will display the number of bombs in it's proximity as described above
5. Using the bomb proximity information from cleared cells, locate and flag all of the bombs and clear non-bomb spaces. Once all bombs are flagged and the non-bomb cells are cleared, the game is over and the player has won!
# Tic Tac Toe Game

This is a simple text-based implementation of the classic Tic Tac Toe game in Python. The game is played in the console, and players take turns making their moves until there is a winner or the board is filled, resulting in a tie.

## Features

- Clear screen before each turn for a clean and user-friendly interface.
- Player input validation to ensure a valid and non-occupied cell is selected.

## How to Play

1. Run the script in a Python environment.
   ```
   python main.py
   ```
2. Players will take turns entering their moves by specifying the row (1-3) and column (1-3) indices.
3. The game will display the current state of the board after each move.
4. The game will continue until there is a winner or the board is full, resulting in a tie.

## Script Details

- `clear_screen()`: Function to clear the terminal screen based on the operating system.
- `print_board(board)`: Function to print the current state of the Tic Tac Toe board.
- `check_win(board)`: Function to check if a player has won by examining rows, columns, and diagonals.
- `is_board_full(board)`: Function to check if the board is full, resulting in a tie.
- `main()`: The main game loop where players make their moves and the game state is updated.

## How to Run

Ensure you have Python installed on your system. Run the script using the command mentioned above, and follow the on-screen instructions to play the game.

Enjoy the game of Tic Tac Toe!

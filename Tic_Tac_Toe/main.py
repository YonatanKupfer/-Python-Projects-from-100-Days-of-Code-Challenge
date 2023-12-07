import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
    print()

def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
        
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def main():
    board = [[' ' for i in range(3)] for j in range(3)]
    current_player = 'X'

    while True:
        # first clear the screen
        clear_screen()
        print_board(board)
        print(f"It is {current_player}'s turn.")
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if board[row][col] != ' ' or row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move! press enter and try again.")
            input()
            continue
        board[row][col] = current_player
        if check_win(board):
            print(f"{current_player} wins!")
            break
        if is_board_full(board):
            print("Tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()

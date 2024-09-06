#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board.
    
    Args:
        board (list of list of str): The 3x3 board to be printed.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Args:
        board (list of list of str): The 3x3 board to be checked.
        
    Returns:
        bool: True if there's a winner, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_tie(board):
    """
    Checks if the game is a tie (i.e., the board is full and there's no winner).
    
    Args:
        board (list of list of str): The 3x3 board to be checked.
        
    Returns:
        bool: True if it's a tie, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return not check_winner(board)

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row not in range(3) or col not in range(3):
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                
                if check_tie(board):
                    print_board(board)
                    print("The game is a tie!")
                    break
                
                # Switch players
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    tic_tac_toe()

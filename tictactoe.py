def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        # Get the player's move
        try:
            row = int(input(f"Player {current_player}, enter your row (0-2): "))
            col = int(input(f"Player {current_player}, enter your column (0-2): "))
            
            if board[row][col] != ' ':
                print("Cell already taken, try again.")
                continue
            
            board[row][col] = current_player
            
            # Check for a winner
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'
        except (IndexError, ValueError):
            print("Invalid input, please enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()


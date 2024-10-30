import random

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to create an empty board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    lines = (
        board +  # rows
        [[board[i][j] for i in range(3)] for j in range(3)] +  # columns
        [[board[i][i] for i in range(3)]] +  # main diagonal
        [[board[i][2 - i] for i in range(3)]]  # anti-diagonal
    )
    
    for line in lines:
        if line[0] != EMPTY and all(cell == line[0] for cell in line):
            return line[0]
    return None

# Check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return -10
    elif winner == PLAYER_O:
        return 10
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Find the best move for the AI
def find_best_move(board):
    best_score = float('-inf')
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
                    
    return best_move

# Main game loop
def play_game():
    board = create_board()
    current_player = PLAYER_X  # Start with X
    
    while True:
        display_board(board)
        if current_player == PLAYER_X:
            print("Player X's turn (random move):")
            move = random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY])
        else:
            print("Player O's turn (AI move):")
            move = find_best_move(board)
        
        if move != (-1, -1):
            board[move[0]][move[1]] = current_player
            winner = check_winner(board)
            if winner:
                display_board(board)
                print(f"Player {winner} wins!")
                break
            if is_board_full(board):
                display_board(board)
                print("It's a tie!")
                break
            current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

# Run the game simulation
if __name__ == "__main__":
    play_game()

import random

# Function to create the game board
def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

# Function to print the game board
def print_board(board):
    size = len(board)
    
    # Print column headers (A, B, C, etc.)
    print("  " + " ".join([chr(65 + i) for i in range(size)]))
    print("  " + "-" * (2 * size - 1))
    
    # Print each row with row numbers and grid cells
    for i in range(size):
        row_label = str(i + 1)
        row_cells = " | ".join(board[i])
        print(f"{row_label} {row_cells} |")

# Function to place a ship on the board
def place_ship(board, size):
    direction = random.choice(['H', 'V'])
    if direction == 'H':
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 3)
        for i in range(3):
            board[row][col + i] = 'S'
    else:
        row = random.randint(0, size - 3)
        col = random.randint(0, size - 1)
        for i in range(3):
            board[row + i][col] = 'S'
# Function to check if a move is valid
def is_valid_move(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])

# Function to check if a guess is a hit
def is_hit(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return True
    else:
        board[row][col] = 'O'
        return False
        
# Function to check if all ships are sunk
def all_ships_sunk(board):
    for row in board:
        if 'S' in row:
            return False
    return True

#  Main game function
def play_game():
    print("Welcome to Battleship!")
    size = int(input("Enter the grid size (e.g., 5 for a 5x5 grid): "))
    
    player_board = create_board(size)
    computer_board = create_board(size)
    
    place_ship(player_board, size)
    place_ship(computer_board, size)

    while True:
        print("\nYour Board:")
        print_board(player_board)

        # Player's move
        while True:
            try:
                row = int(input("Enter row: ")) - 1  # Adjust for 0-based index
                col = ord(input("Enter column (A, B, C, etc.): ").upper()) - 65  # Convert letter to 0-based index
                if not is_valid_move(computer_board, row, col):
                    print("Move is out of bounds! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter valid row and column.")

        if is_hit(computer_board, row, col):
            print("Hit!")
        else:
            print("Miss!")

        if all_ships_sunk(computer_board):
            print("Congratulations! You've sunk all the computer's ships!")
            break

        # Computer's move
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        print(f"Computer attacks at ({row + 1}, {chr(col + 65)})")
        
        if is_hit(player_board, row, col):
            print("Computer hit your ship!")
        else:
            print("Computer missed!")
        
        if all_ships_sunk(player_board):
            print("The computer has sunk all your ships! Game over!")
            break

if __name__ == "__main__":
    play_game()
    
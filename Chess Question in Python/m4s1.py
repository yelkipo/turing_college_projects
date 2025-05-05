import sys 

# Lists to store occupied positions
occupied_positions = []
black_pieces = []

WHITE_INPUT_QUESTION = 'Choose a white piece and its position in the format "piece,position" (example: rook,a4). You can choose either rook or pawn.\n'

# Taking user input for white piece
white_piece_with_position = input(WHITE_INPUT_QUESTION)
white_piece_with_position = white_piece_with_position.split(',')
white_piece = white_piece_with_position[0].strip()
white_position = white_piece_with_position[1].strip()

# Checking if the user chose a valid piece
if white_piece not in ['rook', 'pawn']:
    print('Please choose either "rook" or "pawn".')
    sys.exit()
else:
    occupied_positions.append(white_position)
    print('The white piece was added successfully!')

BLACK_INPUT_QUESTION = 'Choose a black piece and its position in the format "piece,position" (example: rook,a4).\n'  

# Getting black pieces from user
for x in range(16):  
    black_piece_with_position = input(BLACK_INPUT_QUESTION)
    
    if x == 0 and black_piece_with_position.lower() == 'done':
        print('You must provide at least one valid black piece.')
        sys.exit()
    
    if black_piece_with_position.lower() == 'done':
        break

    black_piece_with_position = black_piece_with_position.split(',')
    black_piece = black_piece_with_position[0].strip()
    black_position = black_piece_with_position[1].strip()

    if black_position in occupied_positions:
        print('You cannot put 2 pieces in one cell.')
    else:
        occupied_positions.append(black_position)
        black_pieces.append(black_position)  # Store position and piece type
        print('The black piece was added successfully!')

# Function to check possible captures for a white pawn
def get_pawn_captures(position, black_positions):
    possible_captures = []

    # Extract column letter and row number
    column = position[0]
    row = int(position[1])  

    # Calculate diagonal attack positions
    left_attack = chr(ord(column) - 1) + str(row + 1)  # One step diagonal left
    right_attack = chr(ord(column) + 1) + str(row + 1)  # One step diagonal right

    # Check if there is a black piece at the attack positions
    if left_attack in black_positions:
        possible_captures.append(left_attack)
    if right_attack in black_positions:
        possible_captures.append(right_attack)

    return possible_captures

# Function to check possible captures for a white rook
def get_rook_captures(position, black_positions):
    possible_captures = []
    column = position[0]
    row = int(position[1])

    # Check vertical (up and down)
    for new_row in range(row + 1, 9):  # Upward direction
        move = column + str(new_row)
        if move in black_positions:
            possible_captures.append(move)
            break  # Rook stops at first obstacle

    for new_row in range(row - 1, 0, -1):  # Downward direction
        move = column + str(new_row)
        if move in black_positions:
            possible_captures.append(move)
            break  

    # Check horizontal (left and right)
    for new_col in range(ord(column) - 1, ord('a') - 1, -1):  # Left direction
        move = chr(new_col) + str(row)
        if move in black_positions:
            possible_captures.append(move)
            break  

    for new_col in range(ord(column) + 1, ord('h') + 1):  # Right direction
        move = chr(new_col) + str(row)
        if move in black_positions:
            possible_captures.append(move)
            break  

    return possible_captures

# Determine which pieces the white piece can capture
if white_piece == 'pawn':
    captures = get_pawn_captures(white_position, black_pieces)
else:
    captures = get_rook_captures(white_position, black_pieces)

# Display results
if captures:
    print(f"The {white_piece} at {white_position} can capture: {captures}")
else:
    print(f"The {white_piece} at {white_position} cannot capture any pieces.")

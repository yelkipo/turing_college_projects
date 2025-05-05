# ♟️ White Chess Piece Capture Checker

This is a simple Python script that simulates placing a white chess piece (rook or pawn) on a board and checks which black pieces it can capture based on their positions.

## 🧠 Features

- Accepts user input to place **one white piece** (rook or pawn).
- Allows the user to enter positions of up to **16 black pieces**.
- Ensures **no two pieces** are placed in the same square.
- Calculates and displays which black pieces can be **captured** by the white piece.

## ▶️ How to Use

1. Run the script.
2. When prompted, input the white piece and its position (e.g., `rook,a4`).
3. Enter the black pieces and their positions one by one in the format `piece,position` (e.g., `pawn,b5`).
4. Type `done` when you're finished entering black pieces.
5. The program will output which black pieces (if any) can be captured.

## 🧩 Example

Choose a white piece and its position in the format "piece,position" (example: rook,a4). You can choose either rook or pawn.

rook,a4

Choose a black piece and its position in the format "piece,position" (example: rook,a4).

pawn,a6 bishop,a2 knight,b4 done

The rook at a4 can capture: ['a6', 'a2', 'b4']


## 📌 Rules Modeled

- **Pawn**: Can capture one square diagonally forward (left or right).
- **Rook**: Can capture the first piece it sees in any horizontal or vertical direction.

## 🛠️ Tech Used

- Python (Standard Library)
- Command-line interface (CLI)

## 📌 Notes

- The script does not validate correct chess piece types for black pieces—only the white piece must be `"pawn"` or `"rook"`.
- This is a beginner-friendly script meant for educational purposes and simple simulations.

## 🚀 Future Improvements

- Add support for all piece types (queen, bishop, knight, etc.)
- Implement a GUI or board visualization.
- Add automatic tests or error handling enhancements.



import time

def isNumberInBoard(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False
    startRow = row - (row % 3)
    startCol = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(board, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if board[row][col] != 0:
        return solveSudoku(board, row, col + 1)

    for num in range(1, 10):
        if isNumberInBoard(board, row, col, num):
            board[row][col] = num
            if solveSudoku(board, row, col):
                return board
            board[row][col] = 0

    return False

sudokus = []
current_sudoku = []

with open('Assignment 2 sudoku.txt', 'r') as file:
    for line in file:
        line = line.strip()

        if line.startswith("SUDOKU"):
            if current_sudoku:
                sudokus.append(current_sudoku)
                current_sudoku = []
        elif line == "EOF":
            if current_sudoku:
                sudokus.append(current_sudoku)
            break
        elif line and line[0].isdigit():
            current_sudoku.append([int(char) for char in line])

finalSudokus = []
before = time.time()
for sudoku in sudokus:
    solved = solveSudoku(sudoku, 0, 0)
    if solved:
        finalSudokus.append(solved)
after = time.time()
print(after - before)
i=1
for sudoku in finalSudokus:
    print("\nSudoku ", i, ": ")
    i+=1
    print(sudoku)

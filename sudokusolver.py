board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - ")  # after every 3 rows we want to divide the sections
        for j in range(len(bo[0])):  # gets length of the row, which is
            if j % 3 == 0 and j != 0:
                print("|", end="")  # end = "" --> does not print '/n' so you don't go to the next line, stay on
                # same line when printing
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    # loop through board, find an empty spot and return the coordinates of that location
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i, j)  # returns row and column
    return None


def is_valid(bo, num, pos):
    # check row, column, and sub grid for validity

    # check Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:  # assume we inserted our num already. checks if the any elements in
            # the row are equal to it AND checks that its not the same position we just inserted our num into
            return False
    # check Column
    for i in range(len(bo)):  # loop through every row (going down), check if current column value is equal to
        # number we just inserted AND checks that its not the same position we just inserted our num into
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check Sub grid, determine which of the 9 sub grids we are in.
    box_x = pos[1] // 3  # get our first position (column) and integer divide by 3
    box_y = pos[0] // 3  # gets our row and integer divide by 3
    # loop through box
    for i in range(box_y * 3, box_y * 3 + 3):  # returns the correct indexes to loop for the box after integer division
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve_board(bo):
    # recursively call this function w/in itself. Base case is when the board is full.
    find = find_empty(bo)
    if not find:
        return True  # we have found the solution, since there are no empty cells left, so return True
    else:
        row, col = find
        for i in range (1, 10):  # loop through values 1-9 and check if they are valid solutions within our board.
            if is_valid(bo, i, (row, col)):
                bo[row][col] = i  # adding new value
                if solve_board(bo):  # recursive call, try to finish solution on NEW BOARD, with new value added
                    return True
                bo[row][col] = 0  # if we looped through 1-9 and none work, solve isn't true, so reset last element
                # we added to 0 and try again with another i (value)
        return False


print_board(board)
solve_board(board)

print("\n-----SOLVED BOARD BELOW-----\n")
print_board(board)
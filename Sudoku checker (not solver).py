board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print('board1')
for i in board1:
    print(i)


def isValidSudoku(board):
    # check rows: is board[0][0]=board[0][1]=...=board[0][8] ?
    # is board[1][0]=board[1][1]=...=board[1][8] ?
    # .....
    # is board[8][0]=board[8][1]=...=board[8][8] ?
    for i in range(9):  # i = row#
        for j in range(9):  # j = col#
            if board[i].count(board[i][j]) > 1 and board[i][j] != '.':
                print('Rows Fail')
                return False

    # check cols: is board[0][0]=board[1][0]=...=board[8][0] ?
    # is board[0][1]=board[1][1]=...=board[8][1] ?
    # .....
    # is board[0][8]=board[1][8]=...=board[8][8] ?
    boardT = []
    for i in range(9):
        boardT.append([])
        for j in range(9):
            boardT[i].append(board[j][i])

    print('boardT')
    for i in boardT:
        print(i)

    for i in range(9):  # i = row#
        for j in range(9):  # j = col#
            if boardT[i].count(boardT[i][j]) > 1 and boardT[i][j] != '.':
                print('Columns Fail')
                return False

    # check squares: Row/col index: 0-2, 3-5, 6-8 (*each combo: 9 squares)
    # name squares A-I
    #   A B C
    #   D E F
    #   G H I
    squares = [[board[0][0], board[0][1], board[0][2],
                board[1][0], board[1][1], board[1][2],
                board[2][0], board[2][1], board[2][2]],

               [board[0][3], board[0][4], board[0][5],
        board[1][3], board[1][4], board[1][5],
        board[2][3], board[2][4], board[2][5]],

               [board[0][6], board[0][7], board[0][8],
        board[1][6], board[1][7], board[1][8],
        board[2][6], board[2][7], board[2][8]],

               [board[3][0], board[3][1], board[3][2],
        board[4][0], board[4][1], board[4][2],
        board[5][0], board[5][1], board[5][2]],

               [board[3][3], board[3][4], board[3][5],
        board[4][3], board[4][4], board[4][5],
        board[5][3], board[5][4], board[5][5]],

               [board[3][6], board[3][7], board[3][8],
        board[4][6], board[4][7], board[4][8],
        board[5][6], board[5][7], board[5][8]],

               [board[6][0], board[6][1], board[6][2],
        board[7][0], board[7][1], board[7][2],
        board[8][0], board[8][1], board[8][2]],

               [board[6][3], board[6][4], board[6][5],
        board[7][3], board[7][4], board[7][5],
        board[8][3], board[8][4], board[8][5]],

               [board[6][6], board[6][7], board[6][8],
        board[7][6], board[7][7], board[7][8],
        board[8][6], board[8][7], board[8][8]]]

    #print('squares')
    #for i in squares:
    #    print(i)


    for i in range(9):  # i = row#
        for j in range(9):  # j = col#
            if squares[i].count(squares[i][j]) > 1 and isinstance(squares[i][j], int):
                print('Squares Fail')
                return False
    print('all ok')
    return True

isValidSudoku(board1)
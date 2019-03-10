# 建立由列表组成的列表

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

board = []
for i in  range(3):
    row = ['_'] * 3
    board.append(row)

weird_board = [['_'] * 3] * 3  # 外面的列表包含3个指向同一个列表的引用
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

row = ['_'] * 3
for i in range(3):
    board.append(row)


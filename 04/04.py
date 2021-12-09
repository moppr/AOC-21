with open("04.in") as f:
    infile = f.read().split('\n\n')
    instruc, inboards = infile[0].split(','), infile[1:]
    boards = []

    for board in inboards:
        boards.append([row.split() for row in board.split('\n')])

    def bingo(board):
        print("bingo")
        print(board)
        s = 0
        for row in board:
            for num in row:
                if num != 'x':
                    s += int(num)
        return s

    bingo_count = 0
    num_boards = len(boards)
    for n in instruc:
        for x,board in enumerate(boards):
            if not board:
                continue
            # mark x's
            for i,row in enumerate(board):
                for j,num in enumerate(row):
                    if num == n:
                        board[i][j] = 'x'
            # check for bingo
            for row in board:
                if row.count('x') == 5:
                    if bingo_count+1 == num_boards:
                        print(bingo(board)*int(n))
                        print(boards)
                    #print(bingo(board)*int(n))
                    else:
                        bingo_count += 1
                    boards[x] = []
                    break
            if not board:
                continue
            for i in range(5):
                col = list(zip(*board))[i]
                if col.count('x') == 5:
                    if bingo_count+1 == num_boards:
                        print(bingo(board)*int(n))
                        print(boards)
                    #print(bingo(board)*int(n))
                    else:
                        bingo_count += 1
                    boards[x] = []
                    break

    #print(boards)
    # for board in boards:
    #     if board:
    #         print(board)
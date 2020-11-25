from time import time
import matplotlib.pyplot as plt


def Initialise(n):
    # 2D array of n*n filled with -1
    board = [[-1 for j in range(n)]for i in range(n)]

    # 8 possible moves
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [-1, 2], [1, 2], [-1, -2], [1, -2]] 

    board[0][0] = 0 # first placement
    count = 1 #  variable for next position

    if KnightTour(n, board, moves, [0,0], count): # solvable
        for row in board:
            print(row)
    else:
        print("No solution exists for n = ", n)


def KnightTour(n, board, moves, currentMove, count):
    if count == n*n: # each square is visited
        return True

    # loop for trying every possible move for safe placement or backtrack to previous safe placement
    for i in range(8):
        # location for next move
        nextMove = [currentMove[0]+moves[i][0], currentMove[1]+moves[i][1]]

        if(SafeMove(nextMove, n, board)): # next move is safe
            board[nextMove[0]][nextMove[1]] = count # placement
            
            # recursive call for next move
            if (KnightTour(n, board, moves, nextMove, count + 1)):
                return True # successful at safe placement
            
            # no safe move, so backtrack
            board[nextMove[0]][nextMove[1]] = -1
    
    return False # unable to find safe moves


def SafeMove(nextMove, n, board):
    #  x and y displacements
    x = nextMove[0]
    y = nextMove[1]

    if x >= 0 and x < n and y >= 0 and y < n: # move is within bound
        if board[x][y] == -1: # square is unvisited
            return True # safe to place
    return False 


if __name__ == "__main__":
    boardSize, timeList = [], []

    for n in range(3, 8):
        boardSize.append(n)
        start = time()
        Initialise(n)
        end = time()
        timeList.append(end - start)
        print("done with ", n)

    print(boardSize)
    print(timeList)
    plt.plot(boardSize, timeList, "g")
    plt.show()

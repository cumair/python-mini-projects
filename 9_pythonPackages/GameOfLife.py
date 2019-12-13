'''

Read the Wikipedia article on Conway’s Game of Life. We will implement this simulation on a torus because
it will make the code easier and we won't need to deal with boundaries. This means that cells on the top
are adjacent to cells on the bottom and the same is true for the left and right sides.

Write a function called conway(s, p) that generates a board, which is a square two dimensional
NumPy array of size s. The board should be randomly populated with probability p. If p is set to 0,
all cells should be 0 (dead). If p is set to 1, all cells should be 1 (alive). Start with p=0.1;
about 10 percent of cells should 1.

Write a function advance(b,t) that accepts a Conway board and advances it t time steps according to the rules:

    • Any live cell (marked as 1) with fewer than two live neighbors dies, as if by underpopulation.
    • Any live cell (marked as 1) with two or three live neighbors lives on to the next generation.
    • Any live cell (marked as 1) with more than three live neighbors dies, as if by overpopulation.
    • Any dead cell (marked as 0) with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to pleasantly display the board.

'''

import numpy as np

# get user input
s = int(input('Enter size of 2D array: '))
p = float(input('Enter probability (p): '))
t = int(input('Enter t time steps of advances: '))


# ******************************************************************************************************
def conway(s, p):                           # s = sizeOfarray  p = probability
    'generates a board randomly populated with p, which is 2D NumPy array of size s'

    array2D = np.random.random((s, s))      # 2D array of size(s,s) with random numbers
    board = array2D + p
    
    return board.astype(int)                # return board with zeros and ones


# ******************************************************************************************************
b = conway(s, p)                            # create a board


# ******************************************************************************************************
def rules(cell, live_n):
    'returns 0(dead) or 1(live) based on Game of Life rules'

    if cell == 0:                           # if value of cell is 0
        if live_n == 3:                     # if there are exactly 3 live neighbors
            return 1                        # survive
        else:                               # if not
            return 0                        # dead

    else:                                   # if value of cell is 1
        if live_n < 2 or live_n > 3:        # if there are <2 live neighbors or >3 live neighbors
            return 0                        # dead
        else:                               # if there are 2 live neighbors or 3  live neighbors
            return 1                        # survive


# ******************************************************************************************************
def sumOfneighbors(b, i, j):                  # b = board,    i = row,    j = column
    'returns sum of neighbors for a value'

    s = len(b[0])                           # length of board
    
    lt, rt = max(0, i-1), min(s+1, i+2)     # left, right
    up, dn = max(0, j-1), min(s+1, j+2)     # up, down
    
    n = b[lt:rt, up:dn]
    
    if b[i,j] == 1:
        return np.sum(n) - 1

    else:
        return np.sum(n)

# ******************************************************************************************************
def new_board():
    'sets global board as new board after applying rules on every cell in global board'

    global b

    s = len(b[0])                           

    new_b = conway(s, 0)                    # new board
    
    N = len(b[0])                           # length of board

    for i in range(N):                      # for row in length of board
        for j in range(N):                  # for column in length of board
            
            new_b[i,j] = rules(b[i,j], sumOfneighbors(b,i,j))

    b = new_b                               # set board as new board


# ******************************************************************************************************
def advance(t):
    'accepts t and advances the board t time steps according to the rules'

    global b

    print('\nGeneration Zero/Original Board:')
    for i in b:
        print(i)

    for i in range(t):
        new_board()

    print('\nGeneration One/Updated Board:')
    for i in b:
        print(i)


# ******************************************************************************************************
advance(t)

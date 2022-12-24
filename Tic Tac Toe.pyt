import random

board = [' ' for x in range(9)]

def insertLetter(letter, pos):
    board[pos] = letter

def isSpaceFree(pos):
    return board[pos] == ' '

def printBoard(board):
    for x in range(0,9,3):
        print(' ' + board[x] + ' | ' + board[x+1] + ' | ' + board[x+2])

def isWinner(bo, le):
    return (bo[6] == le and bo[7] == le and bo[8] == le) or (bo[3] == le and bo[4] == le and bo[5] == le) or(bo[0] == le and bo[1] == le and bo[2] == le) or(bo[0] == le and bo[3] == le and bo[6] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[0] == le and bo[4] == le and bo[8] == le) or(bo[2] == le and bo[4] == le and bo[6] == le)

def playerMove():
    loc = int(input('Please select a position to place an \'X\' (0-8): '))
    if loc >= 0 and loc < 9 and isSpaceFree(loc):
        insertLetter('X', loc)

def selectRandomLoc():
    b = True
    r = random.randrange(0,9)
    while b:
        r = random.randrange(0,9)
        if isSpaceFree(r):
            b = False
    return r
def isBoardFull(board):
    if board.count(' ') == 0:
        return True
    return False


def main1():
    while not(isWinner(board, 'Y') or isWinner(board, 'X') or isBoardFull(board)):
        playerMove()
        printBoard(board)
        insertLetter('Y',selectRandomLoc())
        printBoard(board)
def main2():
    while not(isWinner(board, 'Y') or isWinner(board, 'X') or isBoardFull(board)):
        insertLetter('Y',selectRandomLoc())
        printBoard(board)
        playerMove()
        printBoard(board)

def singlePlayer():
    printBoard(board)
    x = input("Type 0 to go first or 1 to go second: ")
    if (x == 0):
        main1()
    else:
        main2()
    if (isWinner(board,'Y')):
        print("Computer wins")
    elif (isWinner(board,'X')):
        print("User wins")
    print("game over")


def simulation():
    while not(isWinner(board, 'Y') or isWinner(board, 'X') or isBoardFull(board)):
        insertLetter('X',selectRandomLoc())
        if (isWinner(board, 'Y')):
            print("Y wins")
            break
        elif (isWinner(board,'X')):
            print("X wins")
            break
        elif (isBoardFull(board)):
            print("tie game")
            break
        else:
            insertLetter('Y',selectRandomLoc())
        
    printBoard(board)

singlePlayer()
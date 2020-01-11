import random
rows= int(input("How many rows would u like? "))
columns= int(input("How many columns would u like? "))
board=[]
for i in range(rows):
    subBoard=[]
    for j in range(columns):
        subBoard.append('')
    board.append(subBoard)

def printBoard():
    for i in board:
        for j in i:
            print(j,end=" ")
        print()

def startFinish():
    board[1][0] = "."
    board[1][1]="."
    board[rows-2][columns-1] = "."
    board[rows-2][columns-2] = "."

def randomDir():
    r = random.randrange(0,2)
    if r == 0:
        return 'turn'
    else:
        return 'stay'

def randomDot_2():
    leftLastTurn=0
    right=columns-1
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if j != leftLastTurn:
                if randomDir() == 'turn':
                    if board[i][j-1] == '.':
                        if i == 1:
                            board[i+1][j] = '.'
                        if i == rows-1:
                            board[i-1][j]= '.'
                        else:
                            if randomDir() == 'turn':
                                board[i+1][j] = '.'
                            else:
                                board[i-1][j] = '.'     
                    if board[i-1][j] == '.':
                        if j == 1:
                            board[i][j+1] = '.'
                        if j == columns-1:
                            board[i][j-1]= '.'
                        else:
                            if randomDir() == 'turn':
                                board[i][j+1] = '.'
                            else:
                                board[i][j-1] = '.'   
                    leftLastTurn = j+1
                else:
                    if board[i-1][j] == '.':
                        board[i+1][j] == '.'
                    else:
                        board[i][j+1]="."
            else:
                if board[i-1][j] == '.':
                    board[i+1][j] == '.'
                else:
                    board[i][j+1]="."
            

def cleanUp():
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            # top and bottom frame
            # score_1=0
            # score_2=0
            # score_3=0
            # score_4=0
            # score_5=0
            # score_6=0
            if i == 1:
                board[0][j-1]= ''
                board[0][columns-1]= ''
                board[rows-1][j-1]= ''
                board[rows-1][columns-1]= ''
            # if j <= columns-4:
            #     if board[i][j] == '.' and board[i][j+1] == '.' and board[i][j+2] == '.':
            #         if (board[i+1][j] == '.' and board[i+1][j+1] == '.' and board[i+1][j+2] == '.') or (board[i+1][j] == '.' and board[i+1][j+1] == '.' and board[i+1][j+2] == '.'):
            #             for k in range(15):
            #                 board[i][j]=''
            # if i <= rows-4:
            #     if board[i][j] == '.' and board[i+1][j] == '.' and board[i][j] == '.':
            #         if (board[i][j+1] == '.' and board[i+1][j+1] == '.' and board[i+2][j+1] == '.') or (board[i][j+1] == '.' and board[i+1][j+1] == '.' and board[i+2][j+1] == '.'):
            #             board[i][j]=''
            if j <= columns-3 and j >= 2  and i <= rows-3 and i >=2 and board[i][j] == '':
                if board[i+1][j-1] == '' and board[i][j-1] != '' and board[i+1][j] != '':
                    if randomDir() == 'turn':
                        board[i][j-1] = ''
                    else:
                        board[i+1][j] = ''  
                if board[i-1][j-1] == '' and board[i][j-1] != '' and board[i-1][j] != '':
                    if randomDir() == 'turn':
                        board[i][j-1] = ''
                    else:
                        board[i-1][j] = ''    
                if board[i+1][j+1] == '' and board[i][j+1] != '' and board[i+1][j] != '':
                    if randomDir() == 'turn':
                        board[i][j+1] = ''
                    else:
                        board[i+1][j] = ''    
                if board[i-1][j+1] == '' and board[i][j+1] != '' and board[i-1][j] != '':
                    if randomDir() == 'turn':
                        board[i][j+1] = ''
                    else:
                        board[i-1][j] = ''       
                                   


def rand4(i,j):
    r = random.randrange(0,4)
    while True:
        if r == 0 and i != 1:
            return 'up'
        if r == 1 and i != rows-2:
            return 'down'
        if r == 2 and j != 1:
            return 'left'
        if r == 3 and j != columns-2:
            return 'right'
        else:
            r = random.randrange(0,4)


def randomDot_3():
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            result = rand4(i,j)
            if result == 'up':
                # return 'up'
                board[i-1][j] = '.'
            if result == 'down':
                # return 'down'
                board[i+1][j] = '.'
            if result == 'left':
                # return 'left'
                board[i][j-1] = '.'
            if result == 'right':
                # 'right'
                board[i][j+1] = '.'


startFinish()
randomDot_3()
# randomDot_2()
printBoard()
print()
print()
cleanUp()
printBoard()



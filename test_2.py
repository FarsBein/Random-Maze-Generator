import random
import os
rows= int(input("How many rows would u like? "))
columns= int(input("How many columns would u like? "))
showWork= input("whould you like to see the generator in action (y/n)? ")
board=[]
checkedAlready=[]
for i in range(rows):
    subBoard=[]
    for j in range(columns):
        subBoard.append('■')
    board.append(subBoard)

def printBoard():
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    print()

def startFinish():
    board[1][0] = "."
    board[1][1] = "."
    board[1][2] = "."
    board[rows-2][columns-1] = "."
    board[rows-2][columns-2] = "."
    board[rows-2][columns-3] = "."
    board[rows-3][columns-3] = "."

def lastCleanUp():
    print('last Clean Up')
    for  y in range(1,rows-1):
        for x in range(1,columns-1):
            # top and bottom frame
            # if x == 1:
            #     board[y-1][0]= '■'
            #     board[y-1][columns-1]= '■'
            if board[y][x] == '.':
                if board[y][x+1] == '■' and board[y][x-1] == '■' and board[y+1][x] == '■' and board[y-1][x] == '■':
                    result = turn4(x,y,[0,1])
                    board[result[1]][result[0]] = '.'
    board[1][0]='.'

def cleanUp():
    print("clean up")
    filledBox=True
    filledBoxesList=[]
    checkedBox=[]
    finalCheckBox=[]
    boxed=0
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if j <= columns-3 and i <= rows-3 and board[i][j] != '.':
                for r in range(3):
                    for c in range(3):
                        if board[i+r-1][j+c-1]=='■':
                            boxed+=1
                        if board[i+r][j+c] == '.':
                            filledBox=False
            
                if filledBox and i < rows-1 and j < columns-1:
                    board[i+1][j+1] = '.'
                    board[i][j+1] = '.'
                    board[i+1][j] = '.'
                filledBox=True
                # remove corners 
                # if boxed >= 5:
                #     if showWork == 'y':
                #         os.system('cls')
                #         printBoard()
                #         print()
                #     board[i][j] = '.'
                boxed=0
                  

    # print(filledBoxesList)
def DeepCheck(y,x):
    for r in range(3):
        for c in range(3):
            if board[y+r][x+c] == '.':
                return False
    return True
def findStart():
    for y in range(1,rows-3):
        for x in range(1,columns-3):
            if DeepCheck(y,x) and [x,y] not in checkedAlready:
                checkedAlready.append([x,y])
                return [x,y]
    return []
            


def turn4(x,y,possibleTurns):
    TurnIndex = random.randint(0,len(possibleTurns)-1)
    if possibleTurns[TurnIndex] == 0:
        x+=1
    if possibleTurns[TurnIndex] == 1:
        y-=1
    if possibleTurns[TurnIndex] == 2:
        x-=1
    if possibleTurns[TurnIndex] == 3:
        y+=1
    return [x,y]


def randomDot_6(Heads):
    print(Heads)
    currentHead = []
    possibleTurns=[]
    tries=0
    straight=False
    # while True:
    # try: 
    # print(Heads)
    while tries < 2:
        for x,y in Heads:
            # print(f'[x: {x},y: {y}]')   
            if straight and x not in [1,columns-1,0] and y not in [1,rows-1,0]:
                # if [x,y] in [[round(columns/2),round(rows/2)],[2,2],[2,rows-3],[columns-3,rows-3],[columns-3,2]]:
                if board[y][x-1] == '.':
                    x+=1
                elif board[y-1][x] == '.':
                    y+=1
                elif board[y][x+1] == '.':
                    x-=1
                elif board[y+1][x] == '.':
                    y-=1
                Heads.append([x,y])
                # board[x][y] = '.'
                straight=False
                if y <= rows-1 and x <= columns-1:
                    board[y][x] = '.'
            elif y >= 1 and x <= columns-2 and y<=rows-2 and x >=1:
                if (rows-y) > 2 and board[y+1][x] == '■' and board[y+2][x] == '■'and board[y-1][x] != '.':
                    if board[y+1][x+1] == '■' and board[y+1][x-1] == '■' and board[y+2][x+1] == '■' and board[y+2][x-1] == '■':
                        possibleTurns.append(3)
                if board[y-1][x] == '■' and board[y-2][x] == '■' and board[y+1][x] != '.':
                    if board[y-1][x+1] == '■' and board[y-1][x-1] == '■' and board[y-2][x+1] == '■' and board[y-2][x-1] == '■':
                        possibleTurns.append(1)
                if (columns-x) > 2 and board[y][x+1] == '■' and board[y][x+2] == '■' and board[y][x+1] != '.':
                    if board[y+1][x+1] == '■' and board[y-1][x+1] == '■' and board[y+1][x+2] == '■' and board[y-1][x+2] == '■':
                        possibleTurns.append(0)
                if board[y][x-1] == '■' and board[y][x-2] == '■' and board[y][x+1] != '.':
                    if board[y+1][x-1] == '■' and board[y-1][x-1] == '■' and board[y+1][x-2] == '■' and board[y-1][x-2] == '■':
                        possibleTurns.append(2)
                if len(possibleTurns) > 0:
                    currentHead = turn4(x,y,possibleTurns)
                    if Heads[-1] != [currentHead[1],currentHead[0]]:
                        board[currentHead[1]][currentHead[0]] = '.'
                        Heads.append(currentHead)
                    else:
                        currentHead = turn4(x,y,possibleTurns)
                        if Heads[-1] != [currentHead[1],currentHead[0]]:
                            board[currentHead[1]][currentHead[0]] = '.'
                            Heads.append(currentHead)

                    # print(Heads)
                possibleTurns = []
                straight= True            
                if showWork == 'y':
                    os.system('cls')
                    printBoard()
                    print()
        tries+=1
        Heads=[Heads[-1]]

startFinish()

# randomDot_6([[round(columns/2),round(rows/2)]])
# randomDot_6([[2,2]])
# randomDot_6([[columns-3,rows-4]])

# Heads=[[round(columns/2),round(rows/2)],[2,2],[round(columns/3),1],[1,rows-2],[columns-2,rows-2],[columns-2,1],[1,round(rows/2)],[columns-2,round(rows/2)],[round(columns/2),rows-2],[round(columns/2),1],[round(columns/3)+round(columns/3),1],[round(columns/3)+round(columns/3),round(rows/2)],[round(columns/3),round(rows/2)],[round(columns/3)+round(columns/3),rows-1],[round(columns/3),rows-1]]
Heads=[[round(columns/2),round(rows/2)],[2,2],[round(columns/3),0],[0,rows-1],[columns-1,rows-1],[columns-1,0],[0,round(rows/2)],[columns-1,round(rows/2)],[round(columns/2),rows-1],[round(columns/2),0],[round(columns/3)+round(columns/3),0],[round(columns/3)+round(columns/3),round(rows/2)],[round(columns/3),round(rows/2)],[round(columns/3)+round(columns/3),rows-1],[round(columns/3),rows-1]]
for j in Heads:
    randomDot_6([j])

for gen in range(150):
    i = findStart()
    if i != []:
        print("find Start")
        randomDot_6([i])
        printBoard()



# lastCleanUp()
# printBoard()
# cleanUp()
# printBoard()





# not check corners (a box make center dot )
import random
import os
rows= int(input("How many rows would u like? "))
columns= int(input("How many columns would u like? "))
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
    for  y in range(1,rows-1):
        for x in range(1,columns-1):
            # top and bottom frame
            if x == 1:
                board[y-1][0]= '■'
                board[y-1][columns-1]= '■'
            if board[y][x] == '.':
                if board[y][x+1] == '■' and board[y][x-1] == '■' and board[y+1][x] == '■' and board[y-1][x] == '■':
                    result = turn4(x,y,[0,1])
                    board[result[1]][result[0]] = '.'

def cleanUp():
    filledBox=True
    filledBoxesList=[]
    checkedBox=[]
    finalCheckBox=[]
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if j <= columns-3 and i <= rows-3 and board[i][j] != '.': #rows-4
                for r in range(3):
                    for c in range(3):
                        # if r != 0 or c != 0:
                        #     checkedBox.append([i+r,j+c])
                        if board[i+r][j+c] == '.':
                            filledBox=False
                if filledBox and i <= rows-1 and j <= columns-1:
                    if [i,j] not in checkedAlready:
                        # if [i,j] not in finalCheckBox:
                            # print(f'[j: {j},i: {i}]','i < rows-1 : ',i < rows-1,'j < columns-1: ',j < columns-1) 
                        # filledBoxesList.append([i,j])
                        # print('filledBox: ',filledBox,' [i,j] not in checkedAlready', [i,j] not in checkedAlready)
                        # print('i <= rows-1: ',i <= rows-1,i,'j <= columns-1: ', j <= columns-1,j)
                        # print([columns-1,rows-1],f'[j: {j},i: {i}]')
                        checkedAlready.append([i,j])
                        # # print(filledBoxesList)
                        # # for coordinates in checkedBox:
                        # #     checkedAlready.append(coordinates)
                        # printBoard()
                        print([i,j])
                        return [i,j]
                # checkedBox=[]
                filledBox=True
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
    currentHead = []
    possibleTurns=[]
    tries=0
    straight=False
    # while True:
    # try: 
    # print(Heads)

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
                Heads.append(currentHead)
                board[currentHead[1]][currentHead[0]] = '.'
                print(Heads)
            possibleTurns = []
            straight= True            
            os.system('cls')
            printBoard()
            print()
        # tries+=1
        # Heads = Heads[::-1]
        # if tries > 2:
        #     break
# except:
    # print(Heads)
    # return

startFinish()

# randomDot_6([[round(columns/2),round(rows/2)]])
randomDot_6([[2,2]])
randomDot_6([[columns-3,rows-4]])

for gen in range(150):
    i = findStart()
    if i != []:
        randomDot_6([i])

# Heads=[[round(columns/2),round(rows/2)],[2,2],[round(columns/3),2],[2,rows-3],[columns-3,rows-3],[columns-3,2],[2,round(rows/2)],[columns-3,round(rows/2)],[round(columns/2),rows-3],[round(columns/2),2],[round(columns/3)+round(columns/3),2],[round(columns/3)+round(columns/3),round(rows/2)],[round(columns/3),round(rows/2)],[round(columns/3)+round(columns/3),rows-2],[round(columns/3),rows-2]]
# for j in range(rows*columns):
#     i = cleanUp()
#     randomDot_6([i])

lastCleanUp()

printBoard()





# not check corners (a box make center dot )
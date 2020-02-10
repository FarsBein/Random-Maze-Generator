import random
import os
rows= int(input("How many rows would u like ( recommended: 30)? "))
columns= int(input("How many columns would u like ( recommended: 40)? "))
showWork= input("would you like to see the Maze Generator in action (y/n)? ")

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
            
# Generates a random direction (turn in 4 directions)
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
    while tries < 2:
        for x,y in Heads:
            # print(f'[x: {x},y: {y}]')   
            if straight and x not in [1,columns-1,0] and y not in [1,rows-1,0]:
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
                    if Heads[-1] != [currentHead[1],currentHead[0]]:
                        board[currentHead[1]][currentHead[0]] = '.'
                        Heads.append(currentHead)
                    else:
                        currentHead = turn4(x,y,possibleTurns)
                        if Heads[-1] != [currentHead[1],currentHead[0]]:
                            board[currentHead[1]][currentHead[0]] = '.'
                            Heads.append(currentHead)
                possibleTurns = []
                straight= True            
                if showWork == 'y':
                    os.system('cls')
                    printBoard()
                    print(Heads)
        tries+=1
        Heads=[Heads[-1]]

startFinish()

Heads=[[round(columns/2),round(rows/2)],[2,2],[round(columns/3),0],[0,rows-1],[columns-1,rows-1],[columns-1,0],[0,round(rows/2)],[columns-1,round(rows/2)],[round(columns/2),rows-1],[round(columns/2),0],[round(columns/3)+round(columns/3),0],[round(columns/3)+round(columns/3),round(rows/2)],[round(columns/3),round(rows/2)],[round(columns/3)+round(columns/3),rows-1],[round(columns/3),rows-1]]
for j in Heads:
    randomDot_6([j])

for gen in range(150):
    i = findStart()
    if i != []:
        print("find Start")
        randomDot_6([i])

os.system('cls') #clear terminal

print("TRY TO GET IN FROM ONE HOLE AND EXIST FROM ANOTHER. GOOD LUCK!")
print()
printBoard()

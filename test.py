import random
import os
rows= int(input("How many rows would u like? "))
columns= int(input("How many columns would u like? "))
board=[]
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
    board[1][1]="."
    board[1][2]='.'
    board[1][3]='.'
    board[rows-2][columns-1] = "."
    board[rows-2][columns-2] = "."

def randomDir():
    r = random.randrange(0,2)
    if r == 0:
        return 'turn'
    else:
        return 'stay'

def cleanUp():
    filledBox=True
    filledBoxesList=[]
    checkedBox=[]
    finalCheckBox=[]
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            # top and bottom frame
            if i == 1:
                board[0][j-1]= '■'
                # board[0][columns-1]= '■'
                board[rows-1][j-1]= '■'
                # board[rows-1][columns-1]= '■'
            # if j <= columns-4:
            #     if board[i][j] == '.' and board[i][j+1] == '.' and board[i][j+2] == '.':
            #         if (board[i+1][j] == '.' and board[i+1][j+1] == '.' and board[i+1][j+2] == '.') or (board[i+1][j] == '.' and board[i+1][j+1] == '.' and board[i+1][j+2] == '.'):
            #             for k in range(15):
            #                 board[i][j]='■'
            # if j <= columns-2:
            #     if board[i][j] == '.' and board[i+1][j] == '.' and board[i-1][j] == '.' and board[i][j+1] == '.' and board[i][j+1] == '.' and board[i][j-1] == '.' and board[i+1][j+1] == '.' and board[i+1][j-1] == '.' and board[i-1][j-1] == '.' and board[i-1][j+1] == '.':
            #         board[i][j] = '■'
            #         board[i][j+1] = '■'
            #         board[i][j-1] = '■'

            # if i <= rows-4:
            #     if board[i][j] == '.' and board[i+1][j] == '.' and board[i][j] == '.':
            #         if (board[i][j+1] == '.' and board[i+1][j+1] == '.' and board[i+2][j+1] == '.') or (board[i][j+1] == '.' and board[i+1][j+1] == '.' and board[i+2][j+1] == '.'):
            #             board[i][j]='■'
            # if j <= columns-3 and j >= 2  and i <= rows-3 and i >=2 and board[i][j] == '■':
            #     if board[i+1][j-1] == '■' and board[i][j-1] != '■' and board[i+1][j] != '■':
            #         if randomDir() == 'turn':
            #             board[i][j-1] = '■'
            #         else:
            #             board[i+1][j] = '■'  
            #     if board[i-1][j-1] == '■' and board[i][j-1] != '■' and board[i-1][j] != '■':
            #         if randomDir() == 'turn':
            #             board[i][j-1] = '■'
            #         else:
            #             board[i-1][j] = '■'    
            #     if board[i+1][j+1] == '■' and board[i][j+1] != '■' and board[i+1][j] != '■':
            #         if randomDir() == 'turn':
            #             board[i][j+1] = '■'
            #         else:
            #             board[i+1][j] = '■'    
            #     if board[i-1][j+1] == '■' and board[i][j+1] != '■' and board[i-1][j] != '■':
            #         if randomDir() == 'turn':
            #             board[i][j+1] = '■'
            #         else:
            #             board[i-1][j] = '■'       
            if j <= columns-3 and i <= rows-3: #rows-4
                for r in range(3):
                    for c in range(3):
                        if r != 1 or 0 != 1:
                            checkedBox.append([i+r,j+c])
                        if board[i+r][j+c] == '.':
                            filledBox=False
                if filledBox:
                    if [i+1,j+1] not in finalCheckBox:
                        # print(f'[j: {j},i: {i}]','i < rows-1 : ',i < rows-1,'j < columns-1: ',j < columns-1) 
                        if i <= rows-1 and j <= columns-1:
                            filledBoxesList.append([i,j])
                            for coordinates in checkedBox:
                                finalCheckBox.append(coordinates)
                checkedBox=[]
                filledBox=True
    # print(filledBoxesList)
    return filledBoxesList

            
                                                   




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
    # for CrazyLoop in range(2):
    currentHead = []
    possibleTurns=[]
    tries=0
    straight=False
    # while True:
    for x,y in Heads:
        # print(f'[x: {x},y: {y}]')   
        if y <= rows-1 and x <= columns-1:
            board[y][x] = '.'
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
        # if [x,y] in [[round(columns/2),round(rows/2)],[2,2],[2,rows-3],[columns-3,rows-3],[columns-3,2]]:
        #     if y > 2 and x < columns-2 and y<rows-2 and x >2:
        #         print(True,[x,y])
        #     else:
        #         print('{',end=' ')
        #         print([x,y],',',end=' ')
        #         print('y >= 2 ',y >= 2,end=' ')
        #         print('x <= columns-2 ',x <= columns-2,end=' ')
        #         print('y <= rows-2 ',y<=rows-2,end=' ')
        #         print('x >= 2 ',x >=2,end=' ')
        #         print('}')
        elif y >= 2 and x <= columns-2 and y<=rows-2 and x >=2:
            if rows-y > 2 and board[y+1][x] == '■' and board[y+2][x] == '■':
                if board[y+1][x+1] == '■' and board[y+1][x-1] == '■': #and board[y+2][x+1] == '■' and board[y+2][x-1] == '■':
                    possibleTurns.append(3)
            if board[y-1][x] == '■' and board[y-2][x] == '■':
                if board[y-1][x+1] == '■' and board[y-1][x-1] == '■': #and board[y-2][x+1] == '■' and board[y-2][x-1] == '■':
                    possibleTurns.append(1)
            if columns-x > 2 and board[y][x+1] == '■' and board[y][x+2] == '■':
                if board[y+1][x+1] == '■' and board[y-1][x+1] == '■': #and board[y+1][x+2] == '■' and board[y-1][x+2] == '■':
                    possibleTurns.append(0)
            if board[y][x-1] == '■' and board[y][x-2] == '■':
                if board[y+1][x-1] == '■' and board[y-1][x-1] == '■': #and board[y+1][x-2] == '■' and board[y-1][x-2] == '■':
                    possibleTurns.append(2)
            if len(possibleTurns) > 0:
                currentHead = turn4(x,y,possibleTurns)
                Heads.append(currentHead)
                # print(currentHead)
            possibleTurns = []
            straight= True

            # os.system('cls')
            # printBoard()
        # tries+=1
        # Heads = Heads[::-1]
        # if tries > 2:
        #     break

startFinish()

Heads = randomDot_6([[round(columns/2),round(rows/2)]])
printBoard()

print()

secHeads = cleanUp()
copyHead=[]
counter=0
for i in range(100):
    secHeads = cleanUp()
    if secHeads == copyHead:
        counter+=1
    if counter > 100:
        break
    for i in secHeads:
        randomDot_6([i])
    copyHead = secHeads

printBoard()


for  y in range(1,rows-1):
    for x in range(1,columns-1):
        if board[y][x] == '.':
            if board[y][x+1] == '■' and board[y][x-1] == '■' and board[y+1][x] == '■' and board[y-1][x] == '■':
                result = turn4(x,y,[0,1])
                board[result[1]][result[0]] = '.'

printBoard()






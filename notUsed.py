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

def randomDot_4():
    areaAroundY=[]
    areaAroundX=[]
    counter=0
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if i >= 2 and j >= columns-2 and i>=rows-2 and j >=2: 
                if board[i+1][j] == '' and board[i+2][j] != '.': # and board[i+2][j+1]
                    areaAroundY.append(0)
                    areaAroundX.append(-1)
                if board[i-1][j] == '' and board[i-2][j] != '.':
                    areaAroundY.append(0)
                    areaAroundX.append(1)
                if board[i][j+1] == '' and board[i][j+2] != '.':
                    areaAroundY.append(1)
                    areaAroundX.append(0)
                if board[i][j-1] == '' and board[i][j-2] != '.':
                    areaAroundY.append(-1)
                    areaAroundX.append(0)

            if len(areaAroundX)>0 or len(areaAroundY):
                randomDirection_1(i,j,areaAroundX,areaAroundY)
                counter+=1
            areaAroundX=[]
            areaAroundY=[]
            if counter > 100:
                break




def randomDot_5():
    checkedSpots=[[round(rows/2),round(columns/2)]]
    checkedSpotsLen=1
    areaAroundX=[]
    areaAroundY=[]
    counter=0
    possibleToRun = True
    while possibleToRun:
        for spotNum in range(len(checkedSpots)-1):
            i = checkedSpots[spotNum][0]
            j = checkedSpots[spotNum][1]
            if i >= 2 and j < columns-2 and i<rows-2 and j >=2:
                if board[i+1][j] == '' and board[i+2][j] != '.' and board[i+2][j+1] != '.' and board[i+2][j-1] != '.':
                    areaAroundY.append(0)
                    areaAroundX.append(-1)
                if board[i-1][j] == '' and board[i-2][j] != '.' and board[i-2][j+1] != '.' and board[i-2][j-1] != '.':
                    areaAroundY.append(0)
                    areaAroundX.append(1)
                if board[i][j+1] == '' and board[i][j+2] != '.' and board[i+1][j+2] != '.' and board[i-1][j+2] != '.':
                    areaAroundY.append(1)
                    areaAroundX.append(0)
                if board[i][j-1] == '' and board[i][j-2] != '.' and board[i+1][j-2] != '.' and board[i-1][j-2] != '.':
                    areaAroundY.append(-1)
                    areaAroundX.append(0)
                if len(areaAroundX) > 0 or len(areaAroundY) > 0:
                    i,j = randomDirection_1(i,j,areaAroundX,areaAroundY)
                    checkedSpots.append([i,j])
                areaAroundX=[]
                areaAroundY=[]
        print(checkedSpots)
        counter+=1
        if counter > 50:
            possibleToRun= False



def randomDirection_1(i,j,areaAroundX,areaAroundY):
    upDown = random.randint(0,2)
    y=i
    x=j
    try:
        if len(areaAroundX) > 0:
            r = random.randint(0,len(areaAroundX)-1)
            if areaAroundX[r] == 0:
                if upDown == 0:
                    x+=1
                    board[i][j+1] = '.'
                else:
                    x-=1
                    board[i][j-1] = '.'
            if areaAroundX[r] == -1:
                y-=1
                board[i-1][j] = '.'
            if areaAroundX[r] == 1:
                y+=1
                board[i+1][j] = '.'
        elif len(areaAroundY) > 0:
            c = random.randint(0,len(areaAroundY)-1)
            if areaAroundY[c] == 0:
                if upDown == 0:
                    y+=1
                    board[i+1][j] = '.'
                else:
                    y-=1
                    board[i-1][j] = '.'
            if areaAroundY[c] == -1:
                x-=1
                board[i][j-1] = '.'
            if areaAroundY[c] == 1:
                x+=1
                board[i][j+1] = '.'
        return x,y 
    except:
        pass


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

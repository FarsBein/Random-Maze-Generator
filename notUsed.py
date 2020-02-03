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



# for testing
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
                if filledBox and i < rows-1 and j < columns-1:
                    # if [i,j] not in checkedAlready:
                        # if [i,j] not in finalCheckBox:
                            # print(f'[j: {j},i: {i}]','i < rows-1 : ',i < rows-1,'j < columns-1: ',j < columns-1) 
                        # filledBoxesList.append([i,j])
                        # print('filledBox: ',filledBox,' [i,j] not in checkedAlready', [i,j] not in checkedAlready)
                        # print('i <= rows-1: ',i <= rows-1,i,'j <= columns-1: ', j <= columns-1,j)
                        # print([columns-1,rows-1],f'[j: {j},i: {i}]')
                        # checkedAlready.append([i,j])
                        # # print(filledBoxesList)
                        # # for coordinates in checkedBox:
                        # #     checkedAlready.append(coordinates)
                        # printBoard()
                    board[i+1][j+1] = '.'
                    board[i][j+1] = '.'
                    # return [i,j]
                # checkedBox=[]
                filledBox=True
    # print(filledBoxesList)

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
                boxed=0
                  
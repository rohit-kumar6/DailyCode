t = int(input())
res = []
for case in range(t):
    R, C = map(int, input().split())
    ls = []
    for i in range(R):
        row = list(map(int, list(input())))
        ls.append(row)

    building = []
    for i in range(R):
        for j in range(C):
            if ls[i][j] == 1:
                building.append((i,j))

    if building == []:
        building.append((int(R/2),int(C/2)))

    #print(building)

    minn = 1
    minnI = -1
    minnJ = -1
    for i in range(R):
        for j in range(C):
            if ls[i][j] != 1:
                dif = []
                for k in building:
                    dif.append((abs(k[0]-i)+abs(k[1]-j)))
                if -min(dif) < minn:
                    minn = -min(dif)
                    minnI = i
                    minnJ = j
                    ls[i][j] = minn

    # print(ls)
    # print(minn,minnI,minnJ)

    ls[minnI][minnJ] = 1

    #print(ls)

    building.append((minnI,minnJ))

    #print(building)

    minn = 1
    for i in range(R):
        for j in range(C):
            if ls[i][j] != 1:
                dif = []
                for k in building:
                    dif.append((abs(k[0]-i)+abs(k[1]-j)))

                if -min(dif) < minn:
                    minn = -min(dif)
                    ls[i][j] = minn

    # print(ls)
    # print(abs(minn))

    if minn>0:
        minn = 0

    msg = "Case #%d: %d" %(case+1,abs(minn))
    res.append(msg)


for i in res:
    print(i)

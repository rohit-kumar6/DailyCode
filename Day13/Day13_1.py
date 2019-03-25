ls = [ -1, -2, -3, -4, -5 ]


ls.sort()
intrest = []

if ls[0]<0 and ls[1]<0:
    intrest.append(ls[0])
    intrest.append(ls[1])

intrest.append(ls[-1])
intrest.append(ls[-2])
intrest.append(ls[-3])

print(intrest)

if len(intrest) == 3:
    print(intrest[0]*intrest[1]*intrest[2])
else:
    res = []
    for i in range(len(intrest) - 2):
        for j in range(i + 1, len(intrest) - 1):
            for k in range(j + 1, len(intrest)):
                c = intrest[i] * intrest[j] * intrest[k]
                res.append(c)

    print(max(res))
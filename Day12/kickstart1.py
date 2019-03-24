T = int(input())
res = []
for case in range(T):
    n, p = map(int, input().split())
    ls = list(map(int, input().split()))

    ls.sort()
    min_res = []

    for i in range(len(ls)-p+1):
        subset = ls[i:i+p]
        count = 0
        for i in range(len(subset)-1):
            dif = subset[-1] - subset[i]
            count += dif

        min_res.append(count)

    msg = "Case #%d: %d" %(case+1,min(min_res))
    res.append(msg)


for i in res:
    print(i)

A = "dadbc"


lenres = 0
res = ""
if A == "u":
    print(1)

for i in range(len(A)):
    dic = {}
    st = ""
    for j in range(i,len(A)):
        dic[A[j]] = dic.get(A[j], 0) + 1
        if dic[A[j]] == 1:
            st += A[j]
        else:
            break

    if len(st) >= lenres:
        lenres = len(st)
        res = st


print(len(res))
import  math
A  = [2,2,2,1,1,1,1]
dic = {}
for i in A:
    dic[i] = dic.get(i, 0) + 1

max = math.floor(len(A) / 2)
res = 0
for key , val in dic.items():
    if val > max:
        res = key
        max = val

print(res)
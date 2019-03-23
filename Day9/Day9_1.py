ls = [ 10, 22, 9, 33, 21, 50, 41, 60 ]

max = 0
res  = []

for i in range(len(ls)-1):
    p = i
    count = 1
    temp = []
    temp.append(ls[p])
    for j in range(i+1,len(ls)):
        if ls[j] > ls[p]:
            temp.append(ls[j])
            count+=1
            p = j
    if max < count:
        max = count
        res = temp

print(max)
print(res)

#
# t = int(input())
#
# res = []
# for i in range(t):
#     n = input()
#     ls = input().split(" ")
#
#     for j in range(len(ls)):
#         ls[j] = int(ls[j])
#
#     print(ls)
#
#     max = 0
#
#     for i in range(len(ls) - 1):
#         p = i
#         count = 1
#         for j in range(i + 1, len(ls)):
#             if ls[j] > ls[p]:
#                 count += 1
#                 p = j
#         if max < count:
#             max = count
#
#     res.append(max)
#
# for i in res:
#     print(i)
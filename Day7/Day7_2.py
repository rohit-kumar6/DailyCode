n = int(input())
ls = input().split(" ")
ls = ls*2
count = 0
max = 0
for i in ls:
    if i=="1":
        count+=1
    else:
        if max<count:
            max = count
        count = 0

print(max)
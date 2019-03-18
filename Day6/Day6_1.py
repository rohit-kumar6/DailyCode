n = int(input())
b = bin(n)
max = 0
count = 0

for i in b:
    if i=="1":
        count+=1
    else:
        if max< count:
            max = count
        count = 0

print(max)
A = "AAZA"
ls = list(A)
le = len(ls)

sum = 0
for i in ls:
    sum += 26**(le-1) * ((ord(i)%65)+1)
    le -= 1

print(sum)
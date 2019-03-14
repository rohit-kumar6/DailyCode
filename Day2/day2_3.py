st1 = input("Enter first string")
str2 = input("Enter second string")

le1 = len(st1)
le2 = len(str2)

if le2 > le1:
    count = le2-le1
    r = le1
else:
    count = le1 - le2
    r = le2

for i in range(r):
    if st1[i] != str2[i]:
        count+=1

print("Hamming Distance",count)
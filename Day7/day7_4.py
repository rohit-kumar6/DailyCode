n = int(input())
str1 = input()
str2 = input()
res = []
res1 = []
count = 0
for i in range(n):
    if str1[i] == "?":
        continue
    elif str1[i] in str2:
        ind = str2.index(str1[i])
        res.append(i+1)
        res1.append(ind+1)
        str2 =  str2[:ind] +"@"+ str2[ind+1:]
        count += 1
    elif "?" in str2:
        ind = str2.index("?")
        res.append(i + 1)
        res1.append(ind + 1)
        str2 = str2[:ind] + "@" + str2[ind + 1:]
        count += 1


while "?" in str1:
    for i in range(n):
        if str2[i]!="@":
            ind = str1.index("?")
            str1 = str1[:ind] + "@" + str1[ind + 1:]
            str2 = str2[:i] + "@" + str2[i + 1:]
            res.append(ind + 1)
            res1.append(i+ 1)
            count+=1
            break

print(count)
for i in range(len(res)):
    print(res[i],res1[i])
st = input()

cvol = 0
dic = {}
for i in st:
    if i in "aeiouAEIOU":
        cvol+=1
    dic[i] = dic.get(i,0) + 1

dic = sorted(dic.items(),reverse=True,key=lambda x: x[1])
print("No of Vowels",cvol)

fre = dic[0][1]
for i in dic:
    if(i[1]==fre):
        print(i)
ls = [10, 15, 3, 7]
k = 17

ls.sort()
first = 0
last = len(ls)
flag = 0

while(first<last):
    sum = ls[first] + ls[last-1]
    if(sum == k):
        flag = 1
        break
    elif(sum > k):
        last-=1
    else:
        first+=1
if flag == 1:
    print("Possible")
else:
    print("Not possible")

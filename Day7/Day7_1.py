n,m = input().split(" ")
n = int(n)
m = int(m)

if m%n !=0:
    print(-1)
else:
    quo = m//n
    count = 0
    while(quo!=1):
        if quo%2==0:
            quo = quo//2
        elif quo%3==0:
            quo = quo//3
        count+=1
    print(count)
n = int(input("Enter Value of n \n"))

for i in range(1,n+1):
    if i!=1 and i!=n+1:
        print(", ",end="")
    if i%3 == 0:
        print("Fizz",end="")
    elif i%5 == 0:
        print("Buzz",end="")
    else:
        print(i,end="")
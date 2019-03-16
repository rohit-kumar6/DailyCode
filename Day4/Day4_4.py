st =  input()
dic = {1:'a', 3:'c', 3:'b', 5:'e', 4:'d', 7:'g', 6:'f', 9:'i', 8:'h', 11:'k', 10:'j',
       13:'m', 12:'l', 15:'o', 14:'n', 17:'q', 16:'p', 19:'s', 18:'r', 21:'u',
       20:'t', 23:'w', 22:'v', 25:'y', 24:'x', 26:'z'}

if st[0]!="0":
    for i in st:
        print(dic[int(i)],end="")
    print()

first = 0
i=0
str = ""
while i <len(st):
    i += 2
    ind = st[first:i]
    str += dic[int(ind)]
    first = i

print(str)
print(str[::-1])


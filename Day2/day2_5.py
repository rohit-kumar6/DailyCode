n = int(input("Length of list"))
ls = []
for i in range(n):
    ls.append(input())

# With Division
mul = 1
for i in ls:
    mul = mul*int(i)
new_ls = [mul]*n
for i in range(n):
    new_ls[i] = new_ls[i] // int(ls[i])

# Witout Division
new_ls = [1]*n
for i in range(n):
    for j in range(n):
        if i!=j:
            new_ls[j] = new_ls[j]*int(ls[i])


print(new_ls)

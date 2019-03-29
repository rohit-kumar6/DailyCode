A = 75
B = 22
upper = 10 ** (A - 1)
lower = 10 ** A

count = 0
for i in range(upper, lower):
    list_of_ints = [int(i) for i in str(i)]
    print(list_of_ints)
    if sum(list_of_ints) == B:
        count += 1

#return count % 1000000007
print(count)
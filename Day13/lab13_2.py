A = [0, 1, 0 ,1]

count = 0
for i in range(len(A)):

    if count%2 == 0:
        if A[i] == 0:
            A[i] = 1
            count+=1
    else:
        if A[i] == 1:
            count+=1



print(count)
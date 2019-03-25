m = [-10, -79, -79, 67, 93, -85, -28, -94]
h = [-2, 9, 69, 25, -31, 23, 50, 78 ]

m.sort()
h.sort()

res = []
for i in range(len(m)):
    res.append(abs(m[i]-h[i]))

print(max(res))
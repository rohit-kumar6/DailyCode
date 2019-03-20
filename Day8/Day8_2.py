"""

Question : Classic Cookie Problem

A two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s.
Each 1 represents choco chip, and each 0 represents other part of cookie.

A choco chip consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
The number of adjacent 1s forming a line determine its size.
Write a function that returns an array of the sizes of all line represented in the input matrix.

Solution Approach :

Used dfs and traverse all the neighbourhood having choco chip

Example :

row = 5
coloum = 5
ls = [[1, 1, 1, 1, 0],
      [1, 0, 1, 0, 0],
      [0, 0, 1, 0, 1],
      [1, 0, 1, 0, 1],
      [1, 1, 1, 1, 0]]
Output = [13,2]

row = 5
coloum = 5
ls = [[1, 0, 0, 1, 0],
      [1, 0, 1, 0, 0],
      [0, 0, 1, 0, 1],
      [1, 0, 1, 0, 1],
      [1, 0, 1, 1, 0]]
Output = [2,2,5,1,2]

"""

print("Enter no of rows")
row = int(input())
print("Enter no of coloums")
coloum = int(input())
print("Enter Element")
ls = [[int(input()) for i in range(row)] for j in range(coloum)]

length = 0 # Global Variable

def dfs(i, j):
    global length
    length = length+1
    ls[i][j] = 0
    if (i + 1 < row):
        if (ls[i + 1][j] == 1):
            dfs(i + 1, j)
    if (i - 1 >= 0):
        if (ls[i - 1][j] == 1):
            dfs(i - 1, j)
    if (j + 1 < coloum):
        if (ls[i][j + 1] == 1):
            dfs(i, j + 1)
    if(j-1 >= 0):
        if (ls[i][j - 1] == 1):
            dfs(i, j - 1)


res = []  # for result
for j in range(coloum):
    for i in range(row):
        if ls[i][j] == 1:
            dfs(i, j)
            res.append(length)
            length = 0

print(res)

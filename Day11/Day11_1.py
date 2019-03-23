def solve(a, b):
  m = (a + b) // 2
  print(m)
  s = input()
  if s == "CORRECT":
    return
  elif s == "TOO_SMALL":
    a = m + 1
  elif s == "TOO_BIG":
    b = m - 1
  elif s == "WRONG_ANSWER":
    exit()
  solve(a, b)

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  _ = int(input())
  solve(a + 1, b)

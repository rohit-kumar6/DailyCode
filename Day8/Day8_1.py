def get_shortest_unique_substring(arr, str):
  minstr = ""
  i = 0
  while i < len(str) - len(arr)+1:
      endindex = i
      while (endindex != len(str)):
          st = str[i:endindex+len(arr)]
          flag = 0
          for k in arr:
              if k not in st:
                  flag = 1
                  break
          if flag == 0:
              if minstr == "":
                  minstr = st
              elif len(minstr) > len(st):
                  if len(st) ==  len(arr):
                    return st
                  minstr = st
              break
          endindex+=1
      i+=1

  return minstr



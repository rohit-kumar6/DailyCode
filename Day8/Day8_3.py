dicta = {"Key1" : "1","Key2" : {"a" : "2","b" : "3","c" : {"d" : "3","e" : {"" : "1"}}}}

output = {}

def fn(d , st):

  for key,val in d.items() :
    if type(d[key]) != dict :
      if st=="":
          output[st+key] = val
      else:
          output[st+"."+key] = val

    else:
      if st == "":
        st = key
      else:
        st += "." + key
      fn(val, st)

fn(dicta, "")
print(output)


#             "Key1" : "1",
#             "Key2.a" : "2",
#             "Key2.b" : "3",
#             "Key2.c.d" : "3",
#             "Key2.c.e" : "1"
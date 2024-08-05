x = input("enter values :")
l = x.split(",")
li = []
for i in l:
    li.append((i))
for y in li:
    if (li.count(y)==1):
        print (y)

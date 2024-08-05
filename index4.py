x = input("enter string : ")
l = x.split(",")
y = input("enter character :")
li=[]
for s in x:
    for r in s:
        if y in s:
            li.append(s)
        else:
            continue
se = set(li)
li1=[]
for q in se:
    li1.append(q)
print(li1)






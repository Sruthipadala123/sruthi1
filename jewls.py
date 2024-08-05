x = input("enter jewels:")
y = input("enter stones: ")
def jewelstones(x, y):
    numjewels = set(x)
    count = 0
    for stone in y:
        if stone in numjewels:
            count+=1
    return count
print(jewelstones(x,y))





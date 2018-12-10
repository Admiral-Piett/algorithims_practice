def maxNum(x):
    if len(x) == 2:
        if x[0] > x[1]:
            return x[0]
        else:
            return x[1]
    recurMax = maxNum(x[1:])
    if x[0] > recurMax:
        return x[0]
    else:
        return recurMax


print maxNum([7,2,28,10,45,13,11,17,25,40,33,32])
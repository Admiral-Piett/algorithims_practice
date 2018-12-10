y = 3141592653589793238462643383279502884197169399375105820974944592
x = 2718281828459045235360287471352662497757247093699959574966967627

print(x * y)

# This needs to be broken down more than just a, b, c, d - I need to understand how to break a number down further for karatsuba
# and then combine
def karatsuba(x, y):
    x = str(x)
    y = str(y)

    if len(x) <= 1 or len(x) <= 1 :
        x = int(x)
        y = int(y)
        return x * y
    else:
        mid = len(x) // 2
        a = x[:mid]
        b = x[mid:]
        c = y[:mid]
        d = y[mid:]

        z0 = karatsuba(a, c)
        z1 = karatsuba(b, d)
        z2 = karatsuba(a, d) + karatsuba(b, c)

        return ((10**len(x)) * z0) + ((10 ** (len(x)//2))*z2) + z1

    # def break_down(i):
    #     mid = int(round(len(str(i)) / 2))
    #     return i[:mid], i[mid:]
    #
    # a, b = break_down(x)
    # c, d = break_down(y)
    #
    # return (10 ** (len(x)/2) * (a * c)) + (10 ** (len(y)/2) * ((a*d)+(b*c))) + (b*d)

print(karatsuba(x, y))
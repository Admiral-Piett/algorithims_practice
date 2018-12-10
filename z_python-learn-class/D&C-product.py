# Uses Karatsuba Multiplication

def binary_product(x,y):
    midX = len(str(x))/2
    midY = len(str(y))/2
    x = str(x)
    y = str(y)
    a = int(x[:midX])
    b = int(x[midX:])
    c = int(y[:midY])
    d = int(y[midY:])
    print 'X ' + str(x) + ' length ' + str(len(str(x)))
    print 'Y ' + str(y) + ' length ' + str(len(str(y)))
    print 'A ' + str(a) + ' length ' + str(len(str(a)))
    print 'B ' + str(b) + ' length ' + str(len(str(b)))
    print 'C ' + str(c) + ' length ' + str(len(str(c)))
    print 'D ' + str(d) + ' length ' + str(len(str(d)))
    
    ac = a * c
    print 'AC ' + str(ac)
    bd = b * d
    print 'BD ' + str(bd)
    group_sum = (a + b) * (c + d)   
    print 'Group Sum ' + str(group_sum)
    sub_4 = group_sum - bd - ac
    print 'Sub 4 ' + str(sub_4)
    
    ac_pad = ac * (10 ** (len(str(x))))
    print 'AC_Pad ' + str(ac_pad)
    sub_4_pad = sub_4 * (10 ** (len(str(x))/2))
    print 'Sub 4 Pad ' + str(sub_4_pad)
    
    return ac_pad + bd + sub_4_pad
    
print binary_product(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)

print 'Test ' + str(3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627)

88871112
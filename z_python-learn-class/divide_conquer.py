def d_f(x):
    if x == []:
        return 0
    else:
        return x.pop(0) + d_f(x)
        
array = [2,3,4,5,6,7,8,9]
     
print d_f(array)

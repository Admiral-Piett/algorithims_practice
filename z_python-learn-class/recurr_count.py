def recurrCount(x):
    if x == []:
        return 0
    else:
        return 1 + recurrCount(x[1:])

        
my_list = []
i = 1

while i < 50:
    my_list.append(i)
    i = i + 1
    
print recurrCount(my_list)
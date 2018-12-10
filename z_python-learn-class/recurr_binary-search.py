def binRecurr(list):
    item = 451
    low = 0
    high = len(list)
    mid = (low + high) /2
    if list[mid] == item:
        print("You got it - " + str(list[mid]))
    
    # if list[mid] == item:
#         print(list[mid])
#         return 
    elif list[mid] < item:
        print(list[mid])
        return binRecurr(list[mid:])
    elif list[mid] > item:
        print(list[mid])
        return binRecurr(list[:mid])

my_list = []
i = 1

while i < 500:
    my_list.append(i)
    i = i + 1
    
# my_num = int(input('What number do you need to want to search for? '))

binRecurr(my_list)
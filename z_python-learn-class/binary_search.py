def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        
        if guess == item:
            print('Got it! It was - ' + str(guess))
            break
        elif guess < item:
            print('Too low ' + str(guess))
            low = mid + 1
        elif guess > item:
            print('Too high ' + str(guess))
            high = mid - 1
    return None

my_list = []
i = 1

while i < 1024:
    my_list.append(i)
    i = i + 1
    
my_num = int(input('What number do you need to want to search for? '))


binary_search(my_list, my_num)
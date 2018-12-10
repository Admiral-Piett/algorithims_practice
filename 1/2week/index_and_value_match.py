import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from week1.merge_sort import merge_sort

def generate_sameple(lower, upper, length):
    return merge_sort(random.sample(range(lower, upper), length))

# Steps
# Find the biggest negative that exists ~ -1
# Get the index of that number and go that index in the array
# If the index is larger than the value found, take the left half of the array and try again
# If the index is less than the value found, take the right half of the array and try again

def find_index_value_match(arr, index):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        index += mid
        check = arr[mid]
        print(mid)
        print(index)
        print(arr[mid], '\n')

        if check >= 0:
            if check > index:
                left = arr[:mid]
                return find_index_value_match(left, index)

            elif check < index:
                right = arr[mid:]
                return find_index_value_match(right, index)
            else:
                print('SUCCESS', check, index)
                return 'SUCCESS', check, index
        else:
            right = arr[mid:]
            find_index_value_match(right, index)



if __name__ == '__main__':
    sample = generate_sameple(-200,200, 200)
    print(len(sample))
    print(sample[199])
    print('sample',sample)
    index = find_index_value_match(sample, 0)
    print(index)
    # print(sample[index])
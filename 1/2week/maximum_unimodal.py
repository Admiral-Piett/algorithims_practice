import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from week1.merge_sort import merge_sort


def generate_unimodal_sample(lower, upper):
    # This generates all unique numbers anyway so the total should always be the length of the range
    arr = random.sample(range(lower, upper), upper)
    arr = merge_sort(arr)
    arr2 = []
    for i in range(1, random.randint(1, len(arr) // 2)):
        j = arr.pop(i)
        arr2.insert(0,j)

    arr.extend(arr2)

    return arr

max_val = 0
def find_max_in_unimodal(arr):
    global max_val
    if len(arr) <= 1:
        return arr
    else:
        print('length', len(arr))
        mid = len(arr) // 2
        check = arr[mid]

        try:
            check_plus_one = arr[mid + 1]
            check_minus_one = arr[mid - 1]

            if check > check_plus_one and check > check_minus_one:
                print('SUCCESS', check)
                return check
            elif check < check_plus_one:
                right = arr[mid:]
                return find_max_in_unimodal(right)
            else:
                # check > check_minus_one
                left = arr[:mid]
                return find_max_in_unimodal(left)
        except:
            if arr[0] > arr[1]:
                print('0',arr[0])
                return arr[0]
            else:
                print('1',arr[1])
                return arr[1]


if __name__ == '__main__':
    sample = generate_unimodal_sample(0, random.randint(0,100000))
    print(sample)
    print(find_max_in_unimodal(sample))
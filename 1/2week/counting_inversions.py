import random
import timeit
# base case
# recursively sort each array
# Can split odd number arrays into either 9 = 4 x 5 or 5 x 4


# Notes:
# So going forward when merging - you're going to want to count all the remaining elements in array B (the first sorted array passed back from all the recurrsive calls)
# when you encounter an inversion (the C element > than the B element), because ALL of the remaining elements will be greater than the C element, because these arrays are sorted.

# Just going to augment the moments when the right array merges to K array and the remaining elements in the i array

# def generate_sameple(lower, upper):
#     # This generates all unique numbers anyway so the total should always be the length of the range
#     return random.sample(range(lower, upper), upper)
#
# sample = generate_sameple(0, 10)
# print(sample)

def read_file(file):
    arr = []
    with open(file) as f:
        for line in f:
            arr.append(int(line.rstrip()))
        return arr

# My biggest problem was not overwriting the variable on every recursive call, so incremement the global scope variable to make it accurate.
inversions = 0

def merge_sort(arr):
    global inversions
    if len(arr) <= 1:
        # print('return', arr)
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)


        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            # print('\n lefti -', i, left[i], ' rightj -', j, right[j])
            if left[i] < right[j]:
                # print('merge lefti', left[i])
                arr[k] = left[i]
                # print('arr k - ', k, arr)
                i += 1
            else:
                # print('merge rightj', right[j])
                arr[k] = right[j]
                # print('arr k - ', k, arr)
                j += 1
                inversions += len(left[i:])

            k += 1

        while i < len(left):
            # print('merge lefti 2', left[i])
            arr[k] = left[i]
            # print('arr k - ', k, arr)
            i += 1
            k += 1

        while j < len(right):
            # print('merge rightj 2', right[j])
            arr[k] = right[j]
            # print('arr k - ', k, arr)
            j += 1
            k += 1
            inversions += len(left[i:])

        return arr, inversions

sample = read_file('files/inversion_integer_array.txt')

print(merge_sort(sample))

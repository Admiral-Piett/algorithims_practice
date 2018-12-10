import random
import timeit
# base case
# recursively sort each array
# Can split odd number arrays into either 9 = 4 x 5 or 5 x 4


# Notes:
# So this works by breaking each array down until it
# if 's in a 1 digit array (len(left) == 1.  After that, it pops up the stack an does the same thing for the right array until len(right) == 1:
# Then it had 2, 1 digit arrays to use.  And we
# if haven if 't been through the merge at all yet, so i, j, & k are all 0:
# So then it compares the 2 and adds them to the original list (which is arr in it's recursed form, down to 2 digits because of the stack), and creates a sorted 2 digit array
# Then it pops up the stack, where it will have another sorted list (after it does the above on the right call at that stack level), but it will again have i, j, & k at 0, so it will iterate through the list again sorting the values between the 2 lists.
# Rinse and repeat up the stack until you have a fully sorted array at the end.


def generate_sameple(lower, upper):
    # This generates all unique numbers anyway so the total should always be the length of the range
    return random.sample(range(lower, upper), upper)

sample = generate_sameple(0, 100)
# print(sample)

def merge_sort(arr):
    if len(arr) <= 1:
        # print('return', arr)
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # print('left', left)
        # print('right', right)

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

        return arr


# print(merge_sort(sample))
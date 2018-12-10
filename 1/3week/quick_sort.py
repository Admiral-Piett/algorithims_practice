import random

# So this version is cool because it does everything in place, and does not require extra memory with all the rest of the arrays

def generate_sameple(lower, upper):
    # This generates all unique numbers anyway so the total should always be the length of the range
    return random.sample(range(lower, upper), upper)

sample = generate_sameple(0, 1000000)
print(sample)

def quick_sort(arr, l, r):

    def pick_pivot(low, high):
        return random.randint(low, high)

    if r - l < 1:
        return arr
    else:
        # Element upon which we compare all the elements to partition on
        pivot = arr.pop(pick_pivot(l, r))
        # index of the element after which all of the elements less than the pivot exist, So pivot == 5, i is index of element after 4
        i = l
        for j in range(l, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            else:
                continue
        arr.insert(i, pivot)
        quick_sort(arr, l, i-1)
        quick_sort(arr, i+1, r)

    return arr



if __name__ == '__main__':
    r_bound = len(sample) - 1
    print(quick_sort(sample, 0, r_bound))
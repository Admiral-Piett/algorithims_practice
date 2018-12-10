def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
        
print quickSort([4,2,6,1,3,5,7])
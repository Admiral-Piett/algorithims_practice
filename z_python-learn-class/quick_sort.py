def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def selectionSort(arr):
    sortedArray = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sortedArray.append(arr.pop(smallest))
    return sortedArray

array = [7,2,28,10,45,13,11,17,25,40,33,32]

print selectionSort(array)
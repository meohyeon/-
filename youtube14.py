n = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(array):
    if len(array) <=1:
        return array
    pivot = array[0]
    aray = array[1:]
    left = [a for a in aray if a <= pivot]
    right = [a for a in aray if a > pivot]
    return quicksort(left) + [pivot]+ quicksort(right)
    
n = quicksort(n)
print(n)
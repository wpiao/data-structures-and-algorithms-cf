# Quick sort
# 1. Select the pivot element - last element in the list
# 2. Rearrange the Array - all the elements in the left side of the pivot element are smaller than it. all the elements in the right side of the pivot element are larger than it.
#   - A pointer is fixed at the pivot element. The pivot element is compared with the elements beginning from the first index.
#   - If the element is greater than the pivot element, a second pointer is set for that element.
#   - If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found eariler.
#   - The process is repeated to set the next greater element as second pointer. And, swap it with another smaller element.
#   - The process goes on until the second last element is reached.
#   - The pivot element is swapped with the second pointer
# 3. Divide sub-list and repeat step 2 on sub-list

def quick_sort(l, left, right):
    if left < right:
        position = find_pivot(l, left, right)
        quick_sort(l, left, position - 1)
        quick_sort(l, position + 1, right)

def find_pivot(l, left, right):
    pivot = l[right]
    low = left - 1
    for i in range(left, right):
        if l[i] <= pivot:
            low += 1
            swap(l, i, low)
    swap(l, right, low + 1)
    return low + 1

def swap(l, i, low):
    temp = l[i]
    l[i] = l[low]
    l[low] = temp

# Testing - python3 
test1 = [5, 10, -10, -5, 0]
quick_sort(test1, 0, 4)
print(test1)
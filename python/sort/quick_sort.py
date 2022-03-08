def quick_sort(l, left, right):
    if left < right:
        position = partition(l, left, right)
        quick_sort(l, left, position - 1)
        quick_sort(l, position + 1, right)

def partition(l, left, right):
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

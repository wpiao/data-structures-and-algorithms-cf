def merge_sort(l):
    n = len(l)
    if n > 1:
        mid = n // 2
        left = l[0:mid]
        right = l[mid:n]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, l)

def merge(left, right, l):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            l[k] = left[i]
            i += 1
        else:
            l[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        l[k:] = right[j:]
    else:
        l[k:] = left[i:]

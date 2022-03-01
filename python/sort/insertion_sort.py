def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        temp = l[i]
        while j >= 0 and temp < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = temp

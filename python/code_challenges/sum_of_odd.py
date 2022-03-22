def sum_of_odd(bst):
    numbers = bst.pre_order()
    sum = 0
    for number in numbers:
        if number % 2 == 1:
            sum += number
    return sum
from sort.insertion_sort import insertion_sort

def test_insertion_sort():
    test1 = [5, 3, 1]
    insertion_sort(test1)
    assert test1 == [1, 3, 5]
    test2 = []
    insertion_sort(test2)
    assert test2 == []
    test3 = [10]
    insertion_sort(test3)
    assert test3 == [10]
    test4 = [2, 3, 1, -10]
    insertion_sort(test4)
    assert test4 == [-10, 1, 2, 3]
    test5 = [-5, -50, -10, -100]
    insertion_sort(test5)
    assert test5 == [-100, -50, -10, -5]

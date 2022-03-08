from sort.quick_sort import quick_sort

def test_quick_sort():
    test1 = []
    quick_sort(test1, 0, 0)
    assert test1 == []

    test2 = [1]
    quick_sort(test2, 0, 0)
    assert test2 == [1]

    test3 = [2,1]
    quick_sort(test3, 0, 1)
    assert test3 == [1,2]

    test4 = [8,4,23,42,16,15]
    quick_sort(test4, 0, 5)
    assert test4 == [4,8,15,16,23,42]

    test5 = [20,18,12,8,5,-2]
    quick_sort(test5, 0, 5)
    assert test5 == [-2,5,8,12,18,20]

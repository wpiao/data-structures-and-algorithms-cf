from sort.merge_sort import merge_sort

def test_merge_sort():
    test1 = []
    merge_sort(test1)
    assert test1 == []

    test2 = [1]
    merge_sort(test2)
    assert test2 == [1]

    test3 = [3,1]
    merge_sort(test3)
    assert test3 == [1,3]

    test4 = [8,4,23,42,16,15]
    merge_sort(test4)
    assert test4 == [4,8,15,16,23,42]

    test5 = [20,18,12,8,5,-2]
    merge_sort(test5)
    assert test5 == [-2,5,8,12,18,20]
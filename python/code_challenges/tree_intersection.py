from hashtable.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    tree1_values_list = tree1.pre_order()
    tree2_values_list = tree2.pre_order()
    common_values = []
    hashtable = Hashtable(128)
    for value in tree1_values_list:
        hashtable.add(str(value), True)
    for value in tree2_values_list:
        if hashtable.contains(str(value)):
            common_values.append(value)
    return common_values
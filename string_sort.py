# Dan Wu
# 1/26/2021
# 4c - Modify insertion sort to sorts a list of strings instead of numbers. It shouldn't return anything.
# The sorting should ignore case. For example "Zebra" should come after "apple", "maRker" should come after "marble", etc.
# Name this function string_sort. The resulting list should contain the exact same strings as the original list, but in sorted order.


def string_sort ( list ):
    """sort a list of strings"""
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i].lower())
        list = new_list



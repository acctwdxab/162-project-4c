# Dan Wu
# 1/26/2021
# 4c - Modify insertion sort to sorts a list of strings instead of numbers. It shouldn't return anything.
# The sorting should ignore case. For example "Zebra" should come after "apple", "maRker" should come after "marble", etc.
# Name this function string_sort. The resulting list should contain the exact same strings as the original list, but in sorted order.


def string_sort ( l ):
    """sort a list of strings"""
    list1 = []
    for i in range(len(l)):
        list1.append(l[i].lower())
        l = list1

    for i in range (1,len(l)):
        key = l[i]
        j = i

    while ( j > 0 and l [j - 1] > key ):
        l[j] = l[j-1]
        j -= 1
        l[j] = key
        return l


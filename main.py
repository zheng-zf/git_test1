# -*- coding: utf-8 -*-

def quick_sort(array, low, high):
    if high > low:
        flag = pretreat_quick_sort(array, low, high)
        # 选一个参考值，左边为比其小的，右边为比其大的
        quick_sort(array, low, flag - 1)
        quick_sort(array, flag + 1, high)
        # 对左右分别进行递归


def pretreat_quick_sort(array, low, high):
    array_flag = array[low]
    while low < high:
        while array[low] < array_flag and low < high:
            low += 1
        while array[high] >= array_flag and low < high:
            high -= 1
        # 有一个小于flag的low+1，有一个大于的high-1
        if low < high:
            array[low], array[high] = array[high], array[low]
    return low


array = [1, 2, 9, 8, 4, 5, 6, 7, 8, 8]
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)

# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/26 14:43


"""
二分查找

算法前提：数据是有序的， 是顺序表结构也就是数组

时间复杂度：O(logn)
"""


"""
二分查找 递归写法
"""
def bsearch_deep(ls, left, right, data):
    if left <= right:
        mid_index = left + (right-left)//2
        if ls[mid_index] == data:
            return mid_index
        elif ls[mid_index] > data:
            return bsearch_deep(ls, left, mid_index-1, data)
        else:
            return bsearch_deep(ls, mid_index+1, right, data)
    else:
        return False


if __name__ == "__main__":
    ls = [1, 3, 5, 7, 9, 17, 29, 30, 77]
    print(bsearch_deep(ls, 0, len(ls)-1, 17))



"""
二分查找 非递归写法
"""

def bsearch(ls, data):
    """二分查找， 非递归"""
    n = len(ls)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        if ls[mid] == data:
            return mid
        elif data < ls[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    ls = [1, 3, 5, 7, 9, 17, 29, 30, 77]
    print(bsearch(ls, 17))
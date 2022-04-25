# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/22 18:55


"""
插入排序原理：
    对于未排序的数据，在已排序序列中从后向前扫描，找到相应位置并插入。（在“找位置”时，从有序序列的后面开始比较，若大则不移动，小则交换位置，再往前比较）

算法特点：
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    时间复杂度：「最好：O(n)」「最坏：O(n^2)」「平均：O(n^2)」
    原地排序
    稳定性：稳定排序
"""


def insert_sort(ls):
    n = len(ls)

    for i in range(1, n):
        j = i
        while j > 0:
            if ls[j] < ls[j-1]:
                ls[j], ls[j-1] = ls[j-1], ls[j]
                j -= 1
            else:
                break
    return ls

if __name__ == "__main__":
    ls = [17, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(ls)
    insert_sort(ls)
    print(ls)
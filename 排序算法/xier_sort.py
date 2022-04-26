# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/26 10:11


"""
希尔排序

希尔排序也是一种插入排序，它是简单插入排序经过改进之后的一个更高效的版本，也称为缩小增量排序。但希尔排序是非稳定排序算法

希尔排序的基本思想是：
    把记录按步长 gap 分组，对每组记录采用直接插入排序方法进行排序。随着步长逐渐减小，所分成的组包含的记录越来越多，当步长的值减小到 1 时，整个数据合成为一组，构成一组有序记录，则完成排序。

算法特点：
    时间复杂度：O(n^1.3)
    空间复杂度：O(1)
    原地排序
    稳定性：不稳定排序
"""


def xier_sort(ls):

    n = len(ls)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j > 0:
                if ls[j] < ls[j - gap]:
                    ls[j], ls[j - gap] = ls[j - gap], ls[j]
                    j -= gap
                else:
                    break

        gap //= 2


if __name__ == "__main__":
    ls = [17, 54, 26, 93, 17, 77, 31, 44, 55, 20, 27]
    print(ls)
    xier_sort(ls)
    print(ls)
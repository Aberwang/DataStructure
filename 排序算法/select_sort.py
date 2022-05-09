# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/25 17:02


"""
选择排序

选择排序算法基本思想：
    在长度为N的无序数组中，第一次遍历n-1个数，找到最小的数值与第一个元素交换；
    第二次遍历n-2个数，找到最小的数值与第二个元素交换；
    ......
    第n-1次遍历，找到最小的数值与第n-1个元素交换，排序完成。

算法特点：
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    时间复杂度：「最好：O(n^2)」「最坏：O(n^2)」「平均：O(n^2)」
    原地排序
    稳定性：不稳定排序
"""


def select_sort(ls):
    n = len(ls)
    if n <= 1:
        return ls

    # 需要进行n-1次选择操作
    for i in range(n-1):
        min_index = i

        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if ls[min_index] > ls[j]:
                min_index = j

        # 一次循环结束，如果有比i位置小的元素，i位置元素和此时min_index位置元素进行交换
        if min_index != i:
            ls[i], ls[min_index] = ls[min_index], ls[i]

    return ls


if __name__ == "__main__":
    ls = [17, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(ls)
    select_sort(ls)
    print(ls)



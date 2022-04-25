# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/25 17:13


"""
归并排序

归并算法的基本思想：
    假设初始序列含有n个记录，则可以看成是n个有序的子序列，每个子序列的长度为1，然后两两归并，得到[n/2]个长度为2或1的有序子序列；再两两归并，......，如此重复直到得到一个长度为n的有序序列为止。

归并排序的执行效率与要排序的原始数组的有序程度无关，所以其时间复杂度是非常稳定的，不管是最好情况、最坏情况，还是平均情况，时间复杂度都是 O(nlogn)

算法特点：
    时间复杂度：O(nlogN)
    空间复杂度：O(n)
    时间复杂度：「最好：O(nlogN)」「最坏：O(nlogN)」「平均：O(nlogN)」
    原地排序
    稳定性：稳定排序

注意：归并排序产生新列表，原列表并未修改。
"""


def merge_sort(ls):
    n = len(ls)
    if n <= 1:
        return ls

    mid = n//2

    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(ls[:mid])

    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(ls[mid:])

    # 将两个有序的子序列合并为一个新的整体
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    ls = [17, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(ls)
    result = merge_sort(ls)
    print(result)
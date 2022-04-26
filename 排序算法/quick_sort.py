# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/25 17:37


"""
快速排序

快速排序算法思想：
1.选取一个数字作为基准，（基数可以随机取，也可选取首位数字）
2.从数列第一位开始，依次与此数字比较，如果小于此数，将小数交换到左边，最后达到小于基准数的在左边，大于基准数的在右边，分为两个数组
3.分别对两个数组重复上述步骤

算法特点：
    时间复杂度：O(nlogn)
    空间复杂度：O(1)
    时间复杂度：「最好：O(nlogn)」「最坏：O(n^2)」「平均：O(nlogn)」
    原地排序
    稳定性：不稳定排序
"""


def quick_sort(ls, low, high):
    if low >= high:
        return ls

    mid_data = ls[low]
    left = low
    right = high

    while left < right:

        while ls[right] >= mid_data and left < right:
            right -= 1
        ls[left] = ls[right]

        while ls[left] <= mid_data and left < right:
            left += 1
        ls[right] = ls[left]

    ls[left] = mid_data

    quick_sort(ls, low, left-1)
    quick_sort(ls, left+1, high)


if __name__ == "__main__":
    ls = [17, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(ls)
    quick_sort(ls, 0, len(ls)-1)
    print(ls)




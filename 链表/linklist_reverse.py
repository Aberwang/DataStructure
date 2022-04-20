# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/20 15:35

"""
单链表反转
方法一：遍历链表后倒序输出
方法二：while循环，在遍历的时候修改指针指向完成反转
方法三：单链表反转的递归写法
"""


class Node:
    def __init__(self, data):
        self.elem = data
        self.next = None

# 打印单链表
def print_linlist(head):
    cur = head
    while cur:
        print(cur.elem, end=" ")
        cur = cur.next
    print()


"""
方法一：遍历链表后倒序输出
时间复杂度：O(n)；空间复杂度：O(n)
空间复杂度高，舍弃此方法
"""

"""
方法二：while循环，在遍历的时候修改指针指向完成反转
时间复杂度：O(n)；空间复杂度：O(1)
"""
def reverse_linklist(head):
    if head == None or head.next == None:
        return head
    # 定义一个变量cur，作为记录当前结点的变量
    cur = head
    # 记录当前结点的前结点的变量
    prev = None
    while cur:
        # 首先需要记下当前节点的下一节点，防止断链
        pnext = cur.next
        # 开始反转：将当前结点的next指针指向他的前结点
        cur.next = prev
        # 继续下一次循环需要更改cur和prev的值
        # 此时的前结点prev的值为：cur
        prev = cur
        # 为了继续遍历，需要将当前结点cur往后移
        cur = pnext
    return prev



"""
方法三：单链表反转的递归写法
"""
def reverse_list(head):
    if head is None or head.next is None:
        return head

    new_list = reverse_list(head.next)
    p1 = head.next
    p1.next = head
    head.next = None
    return new_list


if __name__ == "__main__":
    node_list = Node(1)
    node_list.next = Node(3)
    node_list.next.next = Node(5)
    node_list.next.next.next = Node(7)
    node_list.next.next.next.next = Node(9)

    ret = reverse_linklist(node_list)
    print_linlist(ret)

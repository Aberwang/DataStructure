# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/22 11:07


"""
求链表的中间结点
"""


class Node:
    # 节点类
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


"""
思路：使用快慢指针法。先将快慢两个指针的起始位置均设置为head节点。接下来，慢指针slow每次走一步，快指针fast每次走两步
"""
def get_center_node(head):
    if head is None:
        return

    fast, slow = head, head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    return slow.data

if __name__ == "__main__":
    link_list = Node(1)
    link_list.next = Node(3)
    link_list.next.next = Node(9)
    link_list.next.next.next = Node(7)
    link_list.next.next.next.next = Node(0)

    print(get_center_node(link_list))    # 9
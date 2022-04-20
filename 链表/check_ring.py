# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/20 16:09

"""
 链表中环的检测
"""


class Node():
    """节点类"""
    def __init__(self, data, next=None):
        self.elem = data
        self.next = next


def check_ring_1(head):
    """
    方法一：遍历链表，直接判重：遍历链表，将走过的节点（对节点id）先判断set中是否存在，存在则结束，有环；不存在，则存入set，继续循环直到节点为None。
    （时间复杂度：O(n)，在set中查找的时间复杂度为1；空间复杂度：O(n)）
    """
    node_set = set()
    cur = head
    while cur:
        if cur in node_set:
            return True
        else:
            node_set.update({cur})
            cur = cur.next
    return False


def check_ring_2(head):
    """
    方法二：快慢指针法，时间复杂度：O(n)；空间复杂度：O(1)
        先将快慢两个指针的起始位置均设置为head节点;
        接下来，慢指针slow每次走一步，快指针fast每次走两步，如果链表中有环的结构，在不断的循环过程中，两个指针总会相遇。
    """
    fast_pointe = head
    slow_pointe = head

    while fast_pointe and slow_pointe:
        fast_pointe = fast_pointe.next.next
        slow_pointe = slow_pointe.next
        if slow_pointe is fast_pointe:
            return True
    return False


if __name__ == "__main__":
    head = Node(data=None)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(check_ring_1(head))    # True
    print(check_ring_2(head))    # True



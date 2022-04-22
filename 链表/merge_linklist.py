# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/21 10:15

"""
合并两个有序链表
"""


class Node:
    """节点类"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def merge_order_linklist(link1, link2):
    # 两个有序链表的合并
    if link1 is None:
        return link2
    if link2 is None:
        return link1

    new_head = Node()
    p = new_head

    while link1 is not None and link2 is not None:
        if link1.data > link2.data:
            new_head.next = link2
            link2 = link2.next
        else:
            new_head.next = link1
            link1 = link1.next
        new_head = new_head.next

    if link1 is None:
        new_head.next = link2
    elif link2 is None:
        new_head.next = link1

    return p.next


def print_linklist(head):
    # 打印链表
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    link1_node1 = Node(1)
    link1_node2 = Node(3)
    link1_node3 = Node(5)
    link1_node4 = Node(17)
    link1_node1.next = link1_node2
    link1_node2.next = link1_node3
    link1_node3.next = link1_node4
    print("link1", end=": ")
    print_linklist(link1_node1)

    link2_node1 = Node(2)
    link2_node2 = Node(4)
    link2_node3 = Node(6)
    link2_node4 = Node(8)
    link2_node5 = Node(10)
    link2_node1.next = link2_node2
    link2_node2.next = link2_node3
    link2_node3.next = link2_node4
    link2_node4.next = link2_node5
    print("link2", end=": ")
    print_linklist(link2_node1)

    new_linklist = merge_order_linklist(link1_node1, link2_node1)
    print_linklist(new_linklist)    # 1 2 3 4 5 6 8 10 17



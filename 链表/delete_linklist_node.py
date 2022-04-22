# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/22 10:31


"""
删除链表中倒数第k个节点
"""


class Node:
    # 节点类
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

"""
思路：使用两个指针p1、p2，先让P1走n步，然后p1、p2同时走，当p1走到链表末尾时结束，此时p2所指向的节点即为倒数第n个节点
"""
def delete_node(head, k):
    if head is None or k <= 0:
        return False
    fast, slow = head, head

    for i in range(k):
        if fast is not None:
            fast = fast.next
        else:
            return False

    if fast is not None:
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # slow节点的下一节点为倒数第k个节点
        slow.next = slow.next.next
        return head
    else:
        # 此时fast为None，无next方法，需要删除的节点是第一个节点
        slow = slow.next
        return slow


def print_linklist(head):
    # 打印链表
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    node_list = Node(1)
    node_list.next = Node(3)
    node_list.next.next = Node(5)
    node_list.next.next.next = Node(7)
    node_list.next.next.next.next = Node(9)

    new_linklist = delete_node(node_list, 5)
    if new_linklist:
        print_linklist(new_linklist)

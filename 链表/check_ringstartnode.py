# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/20 18:51

"""
判断链表中环的起始节点
"""

class Node:
    """节点类"""
    def __init__(self, data, next=None):
        self.elem = data
        self.next = next


def check_ringstartnode_1(head):
    """
    方法一：遍历链表，直接使用set（对结点id）判重，第一次出现结点id相同的结点即为环的起始节点
    「时间复杂度：O(n)，空间复杂度：O(n)」
    """
    node_set = set()
    cur = head
    while cur:
        if cur in node_set:
            return cur
        else:
            node_set.update({cur})
            cur = cur.next
    return False


def check_ringstartnode_2(head):
    """
    方法二：思路：
    1、使用快慢指针方法。链表中有环，快慢指针相遇的节点一定是在环内
    2、根据相遇的节点遍历环计算出得环中节点的个数m「快指针和慢指针第一次相遇后，我们让一个指针（p1）回到链表头结点的位置，让另一个指针（p2）留在第一次相遇点。然后，现在让两个指针前进速度一致，都一次移动一个节点。那么两个指针就会在入环点再次相遇了！」
    3、知道环的节点总数，找到环入口：先让一个指针p1从根节点开始往后走m(环中节点总个数)步， 然后再让一个指针p2指向头结点，最后让p1和p2同时往后移动，当p1与p2相遇时，此时相遇的节点就是环的入口。
    （p1指针多比p2指针走环的一圈，相遇点刚好在环的入环口）
    「时间复杂度：O(n)；空间复杂度：O(1)」
    """
    fast = head
    slow = head
    while slow and fast:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            # 此时fast和slow位于相遇节点
            fast = head
            while True:
                if fast == slow:
                    return fast
                else:
                    fast = fast.next
                    slow = slow.next


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
    print(node2)    # node2: <__main__.Node object at 0x100da6e80>
    print(check_ringstartnode_1(head))    # node2: <__main__.Node object at 0x100da6e80>
    print(check_ringstartnode_2(head))    # node2: <__main__.Node object at 0x100da6e80>
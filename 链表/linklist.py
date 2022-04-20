# -*- coding: utf-8 -*-
# Author: wl
# Create Time: 2022/4/20 11:16

class Node:
    """节点类"""
    def __init__(self, data):
        self.elem = data
        self.next = None


class LinkList:
    """ 单链表类 """
    def __init__(self):
        # 头结点
        self._head = None

    def is_empty(self):
        # 链表的判空操作
        return self._head == None

    def length(self):
        # 获取链表的长度
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def print_elems(self):
        # 打印所有元素
        cur = self._head
        while cur:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def search(self, data=None, index=None):
        # 链表的查找操作
        # 链表中不存在返回False，存在则返回元素在链表中的位置
        if data and not index:
            # 根据元素查找元素位置
            if self._head == None:
                return False
            cur = self._head
            count = 0
            while cur:
                if cur.elem == data:
                    return count
                count += 1
                cur = cur.next
            return False
        elif index is not None:
            # 根据元素位置查找元素
            if index < 0 or index > self.length():
                return False
            cur = self._head
            count = 0
            while cur:
                if index == count:
                    return cur.elem
                else:
                    cur = cur.next
                    count += 1
            return False

    def add_head(self, data):
        # 在链表首部添加元素
        addhead_node = Node(data)
        if self._head == None:
            self._head = addhead_node
        else:
            addhead_node.next = self._head
            self._head = addhead_node

    def append(self, data):
        # 添加元素操作
        append_node = Node(data)
        cur = self._head
        if not cur:
            # 空链表
            self._head = append_node
        else:
            while cur:
                if not cur.next:
                    cur.next = append_node
                    break
                cur = cur.next

    def insert(self, index, data):
        # 链表的插入操作
        if index <= 0:
            self.add_head(data)
        elif index > self.length():
            self.append(data)
        else:
            insert_node = Node(data)
            cur = self._head
            prev = None
            count = 0
            while cur:
                if count == index:
                    insert_node.next = cur
                    prev.next = insert_node
                prev = cur
                cur = cur.next
                count += 1


    def remove(self, data):
        # 链表的删除操作
        cur = self._head
        prev = None
        count = 0
        while cur:
            if cur.elem == data:
                if count == 0:
                    self._head = cur.next
                    return
                else:
                    prev.next = cur.next
                    return
            prev = cur
            cur = cur.next
            count += 1


if __name__ == "__main__":
    link_list = LinkList()
    print(link_list.is_empty())
    link_list.append(1)
    link_list.append(3)
    link_list.append(5)
    link_list.append(7)
    link_list.append(9)
    link_list.print_elems()
    print(link_list.length())
    print(link_list.is_empty())
    print(link_list.search(data=9))
    print(link_list.search(index=3))
    link_list.add_head(-1)
    link_list.append(0)
    link_list.print_elems()
    link_list.insert(3, 100)
    link_list.insert(3, 77)
    link_list.print_elems()
    link_list.remove(100)
    link_list.print_elems()
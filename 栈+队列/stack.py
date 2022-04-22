# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/22 13:33


"""
两个队列实现一个栈
"""


"""
栈的特点：先进后出，后进先出 (队尾进，队尾出)
栈的操作：入栈(push)、出栈(pop)

队列的特点：先进先出，后进后出 (队尾进，队头出)
队列的操作：入队(enqueue)、出队(dequeue)
"""


"""
入栈：元素入队列A
出栈：判断如果队列A中只有一个元素，则直接出队即为栈的出栈操作，否则，把队A中的元素出队加入队列B，直到A中只有一个元素，再将A中的最后一个元素出队即为栈的出栈操作。最后为了下一次操作方便，将队A队B互换。
"""
class Stack():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        # 入栈操作
        self.queue1.append(data)

        return self.queue1


    def pop(self):
        # 出栈操作
        if len(self.queue1) == 0:
            return
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))

        del_val = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return del_val


if __name__ == "__main__":
    stack = Stack()
    print(stack.push(1))
    print(stack.push(3))
    print(stack.push(5))
    print(stack.pop())
    print(stack.push(7))
    print(stack.pop())
    print(stack.pop())
    print(stack.queue1)


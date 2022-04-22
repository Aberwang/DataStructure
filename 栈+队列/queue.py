# -*- coding: utf-8 -*-
# Author: wangliang
# Create Time: 2022/4/22 15:19

"""
两个栈实现一个队列
"""


"""
入队：元素压入栈A
出队：先判断栈B是否为空，不为空则直接将栈B的栈顶元素出栈；若为空，先判断栈A是否为空，为空队列中无元素，return None，不为空，则将栈A中的元素全部pop出来再push进栈B。
"""

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if len(self.stack2) >= 1:
            return self.stack2.pop(-1)
        elif len(self.stack1) == 0:
            return None
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(100)
    print(queue.dequeue())
    queue.enqueue(5)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
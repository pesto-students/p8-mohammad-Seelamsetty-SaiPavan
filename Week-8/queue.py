class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):

        if self.out_stack.is_empty:
            while self.in_stack.size()>0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.items.pop()

q = Queue2Stacks()
for i in range(5):
    q.enqueue(i)
for i in range(5):
    print(q.dequeue(i))
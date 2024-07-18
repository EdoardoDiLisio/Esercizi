class Queue:
    def __init__(self) -> None:
        self.queue_list = []

    def push(self, x: int):
        self.queue_list.append(x)
    
    def top(self):
        return self.queue_list[0]
    
    def pop(self):
        return self.queue_list.pop(0)
    
    def empty(self):
        return len(self.queue_list) == 0
    


class MyStack:
    def __init__(self) -> None:
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x : int):
        self.queue1.push(x)

    def pop(self):
        x = -1
        while not self.queue1.empty():
            x = self.queue1.pop()
            if not self.queue1.empty():
                self.queue2.push(x)

        while not self.queue2.empty():
            y = self.queue2.pop()
            self.queue1.push(y)

        return x
    
    def top(self):
        while not self.queue1.empty():
            x = self.queue1.pop()
            self.queue2.push(x)

        while not self.queue2.empty():
            y = self.queue2.pop()
            self.queue1.push(y)

        return x
    
    def empty(self):
        return self.queue1.empty()




mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())    # Output: 2
print(mystack.pop())    # Output: 2
print(mystack.empty())  # Output: False
print(mystack.pop())    # Output: 1
print(mystack.empty())  # Output: True
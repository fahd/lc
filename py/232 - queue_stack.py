class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def transfer(self) -> None:
        while len(self.s1):
            self.s2.append(self.s1.pop())
                
    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2):
            return self.s2.pop()
        else:
            self.transfer()
            return self.s2.pop()

    def peek(self) -> int:
        if len(self.s2):
            return self.s2[-1]
        elif len(self.s1):
            return self.s1[0]


    def empty(self) -> bool:
        sumLen = len(self.s1) + len(self.s2)
        return sumLen == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
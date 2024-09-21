class Solution:
    def __init__(self):
        self.l = []
    def loop(self, max:int, curr:int):
        if curr > max:
            return
        self.l.append(curr)
        self.loop(max, curr * 10)
        next = curr + 1
        if next % 10 != 0 and next <= max:
            self.loop(max, next)
    def lexicalOrder(self, n: int) -> List[int]:
        self.loop(n, 1)
        return self.l
#https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
           return (self.fib(N-1) + self.fib(N-2))

class Solution:
    def fib(self, N: int) -> int:
        fibs = [0,1]
        num = 0
        for i in range(2,N+1):
            num = fibs[i-2] + fibs[i-1]
            fibs.append(num)
        return fibs[N]

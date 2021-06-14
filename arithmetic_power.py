# https://leetcode.com/problems/powx-n/
class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1

        if n % 2 == 0:
            return (self.pow(x, int(n/2)) * self.pow(x, int(n/2)))
        else:
            return (self.pow(x, int(n/2)) * self.pow(x, int(n/2)) * x)

    def myPow(self, x: float, n: int) -> float:

        num = self.pow(x, abs(n))
        if n < 0:
            return (1/num)
        else:
            return num

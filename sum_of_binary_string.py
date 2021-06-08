#https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        b = b[::-1]
        a = a[::-1]
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
            short = b
            long_l = a
        else:
            short = a
            long_l = b
        for index in range(diff):
            short += "0"
        print(short)
        prev_carry = 0
        ans = ""

        for index in range(len(short)):
            add = int(short[index]) ^ int(long_l[index]) ^ prev_carry
            tot = int(short[index]) + int(long_l[index]) + prev_carry
            curr_carry = 1 if tot >=2 else 0
            ans += str(add)
            prev_carry = curr_carry
        if prev_carry:
            ans += str(prev_carry)
        return ans[::-1]

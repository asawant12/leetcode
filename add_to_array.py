# https://leetcode.com/problems/add-to-array-form-of-integer/submissions/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        ultimate_no=0
        num.reverse()
        for index, number in enumerate(num):
            ultimate_no += number * pow(10, index)
        ultimate_no+= k
        ultimate_list = []
        while ultimate_no != 0:
            elem = ultimate_no%10
            ultimate_list.insert(0, elem)
            ultimate_no = ultimate_no//10
        return ultimate_list

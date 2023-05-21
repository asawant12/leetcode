# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common={}
        for index, word in enumerate(list1):
            if word in list2:
                list2_index = list2.index(word)
                sum_index = index + list2_index
                if sum_index in common:
                    common[sum_index].append(word)
                else:
                    common[sum_index] = [word]
        common_indexes = list(common.keys())
        min_index = min(common_indexes)
        return common[min_index]

#https://leetcode.com/problems/fruit-into-baskets/
class Solution(object):
    
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        max_fruits = 0
        start_ptr = 0
        end_ptr = -1
        basket =[]
        for tr in tree:
            if len(basket)<2:
                if tr not in basket:
                    basket.append(tr)
            else:
                if tr not in basket:
                    max_fruits = max(max_fruits, len(tree[start_ptr:end_ptr+1]))
                    start_ptr = end_ptr
                    while tree[start_ptr] == tree[start_ptr-1]:
                        start_ptr -=1
                    if basket[0] == tree[start_ptr]:
                        del basket[1]
                    else:
                        del basket[0]
                    basket.append(tr)
            end_ptr += 1
        max_fruits = max(max_fruits, len(tree[start_ptr:end_ptr+1]))
        return max_fruits

#https://leetcode.com/problems/fruit-into-baskets/
class Solution(object):
    
    def find_max(self, trees):
        basket = []
        total_fruits=0
        for tree in trees:
            if tree not in basket:
                if len(basket)<2:
                    basket.append(tree)
                    total_fruits += 1
                else:
                    break
            else:
                total_fruits += 1
        return total_fruits

    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        max_fruits = 0
        if tree.count(tree[0]) == len(tree):
            return len(tree)
        for tr_index in range(len(tree)):
            fruits = self.find_max(tree[tr_index:])
            max_fruits = max(max_fruits, fruits)
        return max_fruits

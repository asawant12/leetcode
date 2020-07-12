# https://leetcode.com/problems/detect-capital/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        else:
            word_list = list(word)
            first = word_list.pop(0)
            word = "".join(word_list)
            if first.isupper() and word.islower():
                return True
            else:
                return False

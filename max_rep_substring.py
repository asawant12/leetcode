# https://leetcode.com/problems/maximum-repeating-substring/submissions/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        start_ptr = 0
        end_ptr = 1
        count = 0
        if len(sequence) == len(word):
            if sequence == word:
                count = 1
        else:
            temp = word
            while word in sequence:
                word = word + temp
                count += 1
        return count

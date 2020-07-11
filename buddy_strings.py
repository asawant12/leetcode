# https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        list_A = list(A)
        list_B = list(B)
        mis_match_index = []
        if len(A) != len(B) or len(A) < 2:
            return False

        first_char = list_A[0]
        for index in range(len(list_A)):
            if list_A[index] != list_B[index]:
                mis_match_index.append(index)

        if len(mis_match_index) == 2:
            temp = list_A[mis_match_index[0]]
            list_A[mis_match_index[0]] = list_A[mis_match_index[1]]
            list_A[mis_match_index[1]] = temp
            if "".join(list_A) == B:
                return True
            else:
                return False
        else:
            if not len(mis_match_index):
                if A.count(A[0]) == len(A):
                    return True
                uniq_el = set(list_A)
                rep_cnt = 0
                for el in uniq_el:
                    if list_A.count(el) >= 2:
                        rep_cnt += 1
                if rep_cnt:
                    return True
            return False

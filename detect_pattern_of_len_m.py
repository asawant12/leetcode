# https://leetcode.com/submissions/detail/1033763168/
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        start_index = 0
        end_index = m
        counter = 1
        first_arr = arr[start_index:end_index]
        while end_index < len(arr):
            start_index_n = end_index
            end_index_n = start_index_n + m
            curr_arr = arr[start_index_n:end_index_n]
            if first_arr == curr_arr:
                counter += 1
                end_index = end_index_n
                if counter == k:
                    return True
            else:
                counter = 1
                start_index += 1
                end_index = start_index + m
                first_arr = arr[start_index:end_index]

        return False

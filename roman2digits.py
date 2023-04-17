class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = { 'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
        }

        answer = 0
        last_roman = ""
        list_of_str = list(s)
        for roman in list_of_str:
            int_no = mapping[roman]
            if roman in ('V', 'X'):
                if last_roman == "I":
                    int_no -= 1
                    answer -= 1
            if roman in ('L', 'C'):
                if last_roman == "X":
                    int_no -= 10
                    answer -= 10
            if roman in ("D", "M"):
                if last_roman == "C":
                    int_no -= 100
                    answer -= 100
            answer += int_no
            last_roman = roman
        return answer

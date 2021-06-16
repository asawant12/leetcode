# https://leetcode.com/problems/integer-to-english-words/

class Solution(object):
    
    def convert(self, inp):
        words = []
        for index in range(len(inp)):
            if inp[index] != 0:
                if index == 1:
                    inp[index] = inp[index] * 10 
                    if inp[index] == 10:
                        inp[index] = inp[index] + inp[index-1]  
                    
                word = self.mapping[inp[index]]
                if index == 2:
                    word += " Hundreed"
                words.insert(0, word)
        return words

        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_lst = []
        words = []
        self.mapping = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety"
        }
        if num in self.mapping:
            return self.mapping[num].title()
        while num:
            num_lst.append(int(num%10))
            num = int(num/10)
       
        unit_mapping = {
            "hundreed": [],
            "thousand": [],
            "million" : [],
            "billion" : []
        };
        
        
        
        total_digits = len(num_lst)
        hundreeds_index = min(total_digits, 3)
        unit_mapping["hundreed"] = num_lst[:hundreeds_index]
        thousands_index = min(total_digits, 6)
        if thousands_index > 3:
            unit_mapping["thousand"] = num_lst[3:thousands_index]
        millions_index = min(total_digits, 9)
        if millions_index > 6:
            unit_mapping["million"] = num_lst[6:millions_index]
        billions_index = min(total_digits, 10)
        if billions_index > 9:
            unit_mapping["billion"] = num_lst[9:]
        answer = []
        for units in ("hundreed", "thousand", "million", "billion"):
            
            word = self.convert(unit_mapping[units])
            if units != "hundreed" and len(unit_mapping[units]) > 0:
                word.append(units)

            answer.insert(0, " ".join(word))
        print(" ".join(answer))
            
        
        
        

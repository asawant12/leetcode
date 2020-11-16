class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {
           'I' : 1,
           'IV' : 4,
           'V' : 5,
           'IX' : 9,
           'X' : 10,
           'XL' : 40, 
           'L' : 50,
           'XC':90, 
           'C' : 100,
           'CD':400, 
           'D' : 500,
           'CM' : 900, 
           'M' : 1000
        }
        
        roman = list(s)
        number = 0
        prev_chars = []
        for char in roman:
            if char in ('V','X','L','C','D','M'):
                if len(prev_chars) != 0:
                    prev_char = prev_chars.pop()
                    new_char = "{0}{1}".format(prev_char,char)
                    if new_char in mapping:
                        number = number - mapping[prev_char]
                        char = new_char
            number = number + mapping[char]
            prev_chars.append(char)
        return number

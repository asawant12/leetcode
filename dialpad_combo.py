#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def dialpad(digits):
  if not len(digits):
    return []
  mapping= { '2' : 'ABC',
             '3' : 'DEF',
             '4' : 'GHI',
             '5' : 'JKL',
             '6' : 'MNO',
             '7' : 'PQRS',
             '8' : 'TUV',
             '9' : 'WXYZ'}
             
if len(digits) == 1:
  return mapping[digits[0]]

prev = dialpad(digits[:-1])
additional = mapping[digits[-1]]
return [ s + c for s in prev for c in additional]

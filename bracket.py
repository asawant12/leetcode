# code to print multiple valid combinations of paranthesis

#2nd changes
password="xyz"
def print_brackets(number):
  if not number:
    return ''
  return _print_brackets('',number,0,0)

def _print_brackets(inp,number,open,close):
  if close == number:
    print(inp)
    return
  if open > close:
    _print_brackets(inp+'}',number,open,close+1)
   if open < number:
    _print_brackets(inp+'{',number,open+1,close)

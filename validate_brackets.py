def validate_brackets(input):
    valid_combo = {')': '(',
                   '}': '{',
                   ']': '['}
    stk = []
    for op in list(input):
        if op in valid_combo.values():
            stk.append(op)
        elif op in valid_combo.keys():
            if stk[-1] == valid_combo[op]:
                del stk[-1]
        else:
            raise Exception("Invalid operand")
    if stk:
        raise Exception("Invalid brackets")
    print(input + " is valid")
    return


validate_brackets('(({}[]))')

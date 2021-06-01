#Take two positive numbers as strings, and return the sum of them. E.g. "3.14" + "0.9" => "4.04".
def padding_zeros(val1, val2, operation):
    diff = len(val1) - len(val2)
    arr = None
    if diff > 0:
        arr = val2
    if diff < 0:
        arr = val1
    for _ in range(abs(diff)):
        if operation == "append":
            arr.append("0")
        elif operation == "insert":
            arr.insert(0,"0")
        else:
            print("invalid operation")
            break
    return

def addition_of_num(num1, num2, carry_over):
    index=0
    answer = []
    num1.reverse()
    num2.reverse()
    for num in num2:
        addition = int(num) + int(num1[index]) + carry_over
        if addition > 9:
            remainder = addition - 10
            carry_over = 1
        else:
            remainder = addition
            carry_over = 0
        answer.insert(0,str(remainder))
        index += 1
    return carry_over, answer

def addition(num1, num2):
    num1_lst = num1.split(".")
    num1_lft = list(num1_lst[0])
    num1_rt = list(num1_lst[1])
    num2_lst = num2.split(".")
    num2_lft = list(num2_lst[0])
    num2_rt = list(num2_lst[1])

    padding_zeros(num1_rt, num2_rt, "append")    
    padding_zeros(num1_lft, num2_lft, "insert")
    answer=[]
    carry_over = 0
    carry_over, rt_addition = addition_of_num(num1_rt,num2_rt, carry_over)
    carry_over, lft_addition = addition_of_num(num1_lft,num2_lft, carry_over)
    carry_over = "1" if carry_over == 1 else ""
    final_answer = carry_over + "".join(lft_addition) + "." + "".join(rt_addition)
    return final_answer

print(addition(num1="3.14", num2="12.09"))

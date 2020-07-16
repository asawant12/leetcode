
def bin_search(arr, num):
  if len(arr) == 1:
    if arr[0] == num:
      return True
    return False
  arr_len = int(len(arr)/2)
  if arr[arr_len] == num:
    return True
  elif arr[arr_len] > num:
    return bin_search(arr[:arr_len], num)
  elif arr[arr_len] < num:
    return bin_search(arr[arr_len:], num) 
  return False


input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

op = bin_search(input, 12)
print(op)

def cal_hash_code(pattern_to_check):
    hash_code_val = 0
    m = len(pattern_to_check)
    for each_val in pattern_to_check:
        assign_char_val = ord(each_val) - ord('a') + 1
        hash_code_val = hash_code_val + (assign_char_val) * (26 ** (m - 1))
        m = m + 1
    return hash_code_val

def assign_char_val_cal(char_val):
    assign_char_val = ord(char_val) - ord('a') + 1
    return assign_char_val

count = 0
str_to_check = "dbaaccaaedba"
# str_to_check = "dbadba"
pattern_to_check = "dba"
len_of_pattern = len(pattern_to_check)
get_first_compare_string = str_to_check[:len_of_pattern]
print(get_first_compare_string)
# calculate the hashcode for pattern
# hash_code_val = 0
# m=1
# for each_val in pattern_to_check:
#     assign_char_val = ord(each_val)-ord('a')+1
#     hash_code_val = hash_code_val + (assign_char_val)* (26**(m-1))
#     m = m+1
hash_code_val = cal_hash_code(pattern_to_check)
print(hash_code_val)

for index in range(len_of_pattern, len(str_to_check)+1):
   get_hash_val = cal_hash_code(get_first_compare_string)
   if get_hash_val == hash_code_val:
       count = count + 1
   list_get_first_string = list(get_first_compare_string)
   remove_the_first = list_get_first_string.pop(0)
   if index == len(str_to_check):
       break
   list_get_first_string.append(str_to_check[index])
   get_first_compare_string = "".join(list_get_first_string)

print(count)


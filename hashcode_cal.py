def cal_hash_code(pattern_to_check):
    hash_code_val = 0
    m = len(pattern_to_check)
    for each_val in pattern_to_check:
        assign_char_val = ord(each_val) - ord('a') + 1
        hash_code_val = hash_code_val + (assign_char_val) * (26 ** (m - 1))
        m = m + 1
    return hash_code_val

print(cal_hash_code('abd'))
print(cal_hash_code('ade'))
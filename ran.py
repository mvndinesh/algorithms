def return_set(lst, set_val):
    result_lst = []
    for index in range(len(lst)):
        get_in_val = int(lst[index])
        i = index + 1
        j = len(lst) - 1
        while i < j:
            if i > j or i == j:
                break
            sum_val = get_in_val + int(lst[i]) + int(lst[j])
            if sum_val == set_val:
                result_lst.append([get_in_val,lst[i],lst[j]])
                i = i + 1
            elif sum_val < set_val:
                i = i + 1
            elif sum_val > set_val:
                j = j-1
    return result_lst

lst = [1,2,3,4,5]
set_val = 9
print(return_set(lst,set_val))
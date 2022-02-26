lst = [4,3,1,2,4]
index = 0
swap = 0
while True:
    if lst[index] == index + 1:
        index = index + 1
    else:
        get_val = lst[index]
        place_value = index + 1
        get_index_place_value = lst.index(place_value)
        lst[index] = lst[get_index_place_value]
        lst[get_index_place_value] = get_val
        swap = swap + 1
    if index == len(lst)-1:
        break
print(swap)


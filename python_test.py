def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    index_one = 0
    index_two = 0
    dict_diff = {}
    while index_one < len(arrayOne) and index_two < len(arrayTwo):
        if index_one == 0 and index_two == 0:
            get_diff = abs(arrayOne[index_one] - arrayTwo[index_two])
            dict_diff[get_diff] = [arrayOne[index_one], arrayTwo[index_two]]
            if arrayOne[index_one] < arrayTwo[index_two]:
                index_one = index_one + 1
            else:
                index_two = index_two + 1
            continue
        if arrayOne[index_one] <= arrayTwo[index_two]:
            get_diff = abs(arrayOne[index_one] - arrayTwo[index_two])
            if (get_diff) < list(dict_diff.keys())[0]:
                dict_diff = {}
                dict_diff[get_diff] = [arrayOne[index_one], arrayTwo[index_two]]
            index_one = index_one + 1
        elif arrayOne[index_one] > arrayTwo[index_two]:
            get_diff = abs(arrayOne[index_one] - arrayTwo[index_two])
            if (get_diff) < (list(dict_diff.keys())[0]):
                dict_diff = {}
                dict_diff[get_diff] = [arrayOne[index_one], arrayTwo[index_two]]
            index_two = index_two + 1
    return list(dict_diff.values())[0]


print(smallestDifference(sorted([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530]), sorted([-1441, -124, -25, 1014, 1500, 660, 410, 245, 530])))

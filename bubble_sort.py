def bubble_sort(my_list):
   for out_index in range(len(my_list)-1,0,-1):
       for index in range(out_index):
           if my_list[index] > my_list[index+1]:
               temp = my_list[index+1]
               my_list[index + 1] = my_list[index]
               my_list[index] = temp
   return my_list

def selection_sort(my_list):

    for outer_index in range(0,len(my_list)-1):
        min_index = outer_index
        for inner_index in range(outer_index+1,len(my_list)-1):
            if my_list[min_index] > my_list[inner_index]:
                min_index = inner_index
        outer_index_val = my_list[outer_index]
        my_list[outer_index] = my_list[min_index]
        my_list[min_index] = outer_index_val
    return my_list


def insertion_sort(my_list):

    for each_item in range(1,len(my_list)):
        temp = my_list[each_item]
        j = each_item - 1
        while temp < my_list[j] and j != -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j = j-1
    return my_list

def merge(my_list1, my_list2):
    combined = []
    i = 0
    j = 0
    while i < len(my_list1) and j < len(my_list2):

        if my_list1[i] < my_list2[j]:
            combined.append(my_list1[i])
            i = i + 1
        else:
            combined.append(my_list2[j])
            j = j + 1
    while i < len(my_list1):
        combined.append(my_list1[i])
        i = i + 1
    while j < len(my_list2):
        combined.append(my_list2[j])
        j = j + 1
    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left),merge_sort(right))










# my_list = [4,2,6,5,1,3]
# print(bubble_sort(my_list))
# print(selection_sort(my_list))
# print(insertion_sort(my_list))
# print(merge([1,2,4,5,6],[3,7,9,10,13]))
print(merge_sort([3,1,2,4,6,5,8,7,10,9]))
print(merge_sort([8, 5, 2, 9, 5, 6, 3]))

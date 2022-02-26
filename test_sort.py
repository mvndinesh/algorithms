def quick_sort(lst):
    for outer_index in range(len(lst)-1,0,-1):
        for index in range(outer_index):
            if lst[index] > lst[index+1]:
                lst[index],lst[index+1] = lst[index+1],lst[index]
    return lst

def selection_sort(lst):
    for index in range(len(lst)):
        min_index = index
        for inner_index in range(index+1,len(lst)):
            if lst[min_index] > lst[inner_index]:
                min_index = inner_index
        lst[index],lst[min_index] = lst[min_index],lst[index]
    return lst

def insertion_sort(lst):
    for index in range(1,len(lst)):
        temp = lst[index]
        j = index -1
        while j != -1:
            if lst[j] > temp:
                lst[j],temp = temp,lst[j]
            j = j -1
    return lst



print(quick_sort([3,1,2,4,6,5,8,7,10,9]))
print(selection_sort([3,1,2,4,6,5,8,7,10,9]))
print(insertion_sort([3,1,2,4,6,5,8,7,10,9]))
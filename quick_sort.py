def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less_than_pivot = [lst[index] for index in range(1,len(lst)) if lst[index] <= pivot]
    greater_than_pivot = [lst[index] for index in range(1,len(lst)) if lst[index] > pivot]
    val = quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
    return val

print(quick_sort([4,2,1,3,5,6,7,8,9]))
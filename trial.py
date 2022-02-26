import heapq
# h = []
# heapq.heappush(h,(5,"sdf"))
# heapq.heappush(h,(6,"ghj"))
# heapq.heappush(h,(1,"fdf"))
# heapq.heappush(h,(7,"fdf"))
# print(heapq.heappop(h))
# print(heapq.heappop(h))

lst = [1,2,3,4,5]
x = -1
k = 4
h = []
for each_val in lst:
    list_val = []
    get_abs_val = each_val-x
    list_val.append(get_abs_val)
    list_val.append(each_val)
    heapq.heappush(h,tuple(list_val))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))







# def split_decorator(function):
#     def wrapper():
#         func = function()
#         split_values = func.split()
#         return split_values
#     return wrapper
#
# def lowercase_decorator(function):
#     def wrapper():
#         func = function()
#         string_lowercase = func.lower()
#         return string_lowercase
#     return wrapper
#
#
# @split_decorator
# @lowercase_decorator
# def hello():
#     return "Hello forld"
#
# print(hello())
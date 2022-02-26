class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
       self.root = None
       self.pre = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value <  temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            elif value == temp.value:
                return False

    def contains(self,value):
        return_flag = False
        temp = self.root
        if temp is None:
            return return_flag
        while temp:
            if value == temp.value:
                return_flag = True
                break
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return return_flag

    def minimum_value(self):
        temp = self.root
        while True:
            if temp.left is None:
                return temp.value
            temp = temp.left

    def depth_first_search_pre_order(self):
        result = []
        def traverse(current_node:Node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

    def depth_first_search_post_order(self):
        result = []
        def traverse(current_node:Node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)

        traverse(self.root)
        return result

    def depth_first_search_in_order(self):
        result = []
        def traverse(current_node:Node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result



    def height_of_tree(self, bst):
        lst = []
        temp = self.root
        def get_height(temp, lst, leftval, rightval):
            if temp.left is not None:
                leftval = leftval + 1
                get_height(temp.left, lst, leftval,rightval)
            if temp.right is not None:
                rightval = rightval + 1
                get_height(temp.right,lst, leftval,rightval)
            lst.append(leftval)
            lst.append(rightval)

        get_height(temp,lst,0,0)
        return lst














    # def insert(self, value):
       # own Method
    #     new_node = Node(value)
    #     insert_left = False
    #     insert_right = False
    #     if self.root is None:
    #         self.root = new_node
    #         return True
    #     temp = self.root
    #     self.pre = temp
    #     while temp:
    #         insert_left = False
    #         insert_right = False
    #         if value < temp.value:
    #             self.pre = temp
    #             temp = temp.left
    #             insert_left = True
    #         elif value > temp.value:
    #             self.pre = temp
    #             temp = temp.right
    #             insert_right = True
    #         elif value == temp.value:
    #             return False

        # if insert_left:
        #     self.pre.left = new_node
        # elif insert_right:
        #     self.pre.right = new_node
        # return self.root

    def print_right(self):
        temp = self.root
        while temp:
            print(temp.value)
            temp = temp.right




bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)
bst.insert(92)
# print(bst.root.right.right.value)
# print(bst.contains(16))
# print(bst.minimum_value())
# print(bst.root.value)


# qu = []
# result = []
# qu.append(bst.root)
#
# # Breadh first search
# while qu:
#     pop_qu_node:Node = qu.pop(0)
#     if pop_qu_node.left is not None:
#         qu.append(pop_qu_node.left)
#     if pop_qu_node.right is not None:
#         qu.append(pop_qu_node.right)
#     result.append(pop_qu_node.value)
# print(result)
# print(bst.depth_first_search_post_order())
# print(bst.depth_first_search_in_order())
print(max(bst.height_of_tree(bst)))
#depth first search















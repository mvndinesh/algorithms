class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
            elif value == temp.value:
                return False

    def get_minimum(self):
        temp = self.root
        while temp:
            val = temp.value
            temp = temp.left
            if temp is None:
                return val

    def pre_order_traverse(self):
        result = []

        def traverse(temp):
            result.append(temp.value)
            if temp.left is not None:
                temp = temp.left
                traverse(temp)
            if temp.right is not None:
                temp = temp.right
                traverse(temp)

        temp = self.root
        traverse(temp)
        return result

    def post_order_traverse(self):
        result = []

        def traverse(temp:TreeNode):
            if temp.left is not None:
                traverse(temp.left)
            if temp.right is not None:
                traverse(temp.right)
            result.append(temp.value)

        temp = self.root
        traverse(temp)
        return result

    def depth_first_search_post_order(self):
        result = []
        def traverse(current_node:TreeNode):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)

        traverse(self.root)
        return result

    def height_of_a_tree(self):
        result = []
        def traverse(temp,left,right):
            if temp.left is not None:
                left = left + 1
                traverse(temp.left,left,right)
            if temp.right is not None:
                right = right + 1
                traverse(temp.right,left,right)
            result.append(left)
            result.append(right)
        traverse(self.root,0,0)
        return result


binary_tree = BinaryTree()
binary_tree.insert(20)
binary_tree.insert(5)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(1)

print(binary_tree.get_minimum())
# print(binary_tree.pre_order_traverse())
print(binary_tree.post_order_traverse())
print(max(binary_tree.height_of_a_tree()))

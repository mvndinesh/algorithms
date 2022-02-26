class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:

    def __init__(self, value):
        new_node = Node(value)
        self.node = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        if not self.tail.next:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length + 1
        return True

    def pop(self):
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.length = self.length - 1
        return temp.value

    def prepend(self, value):
        if self.head:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        self.length = self.length + 1
        return True

    def pop_first(self):
        if self.head:
            temp = self.head
            value = temp.value
            self.head = self.head.next
            temp = None
        self.length = self.length - 1
        return value

    def get(self, index):
        # temp = self.head
        # count = 0
        # while count < index and temp:
        #     temp = temp.next
        #     count = count + 1
        # return temp.value
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):

        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True

    def insert_node(self,index,value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            create_node = Node(value)
            temp = self.head
            pre = temp
            for _ in range(index):
                pre = temp
                temp = temp.next

            pre.next = create_node
            create_node.next = temp
        self.length = self.length + 1
        return True

    def remove_node(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.pop_first()
        else:
            temp = self.head
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = temp.next


    def reverse(self):

        # temp = self.head
        # self.head = self.tail
        # self.tail = temp
        # before = None
        # after = temp.next
        # for _ in range(self.length):
        #     after = temp.next
        #     temp.next = before
        #     before = temp
        #     temp = after

        temp = self.head
        before = None
        after = None
        while temp:
            val = temp.value
            after = temp.next
            temp.next = before
            # after.next = temp
            before = temp
            temp = after
        print(before.value)











    def get_total_nodes(self):
        return self.length



node_list = Linkedlist(4)
# node_list.node.next = Node(5)
node_list.append(6)
node_list.append(7)
# node_list.prepend(8)?print(str(node_list.pop_first())+"popped value")
# node_list.print()
# node_list.pop()
# node_list.set_value(1,10)
# print(node_list.get(0))
# node_list.insert_node(0,5)
# print(node_list.get_total_nodes())
# node_list.remove_node(2)
node_list.reverse()
node_list.print()

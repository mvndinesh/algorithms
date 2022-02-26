class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def print_from_backward(self):
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return self.head
        temp = self.head
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length = self.length + 1

    def pop(self):
        temp = self.tail
        if self.length == 0:
          return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            temp.prev = None
        self.length = self.length - 1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next= self.head
            self.head.prev = new_node
            self.head = new_node
        self.length = self.length + 1
        return self.head

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return temp.value
        else:
            pop_first_value = temp.value
            self.head = temp.next
            self.head.prev = None
            temp = None
        self.length = self.length -1
        return pop_first_value

    def get(self,index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp.value

    def set(self, index, value):

        if index < 0 or index > self.length - 1:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
            temp.value = value

    def insert(self,index,value):
        insert_node = Node(value)
        temp = self.head
        for _ in range(index):
            temp = temp.next
        previous_node = temp.prev
        previous_node.next = insert_node
        insert_node.prev = previous_node
        insert_node.next = temp
        temp.prev = insert_node
        self.length = self.length+1

    def remove(self, index):
        if index < 0 or index > self.length -1 :
            return None
        if index == 0:
            temp = self.head
            temp = temp.next
            self.head = temp
            temp = None
            self.length = self.length - 1
            return True
        if index == self.length-1:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp = None
            self.length = self.length - 1
            return True
        temp = self.head
        for _ in range(index):
            temp = temp.next
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp = None
        return True




dll = DoubleLinkedList(7)
dll.append(8)
dll.append(9)
# dll.prepend(6)
# print(dll.length)
# dll.pop()
# dll.pop()
# dll.pop()

# print("Printing from the backward")
# dll.print_from_backward()
# print("poping first element")
# print(dll.pop_first())
# print("printing from the beginning")
# dll.print()

# dll.set(1,88)
# dll.insert(1,10)
dll.remove(2)
print(dll.print())
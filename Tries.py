class Node:
    def __init__(self):
        self.children = {}
        self.endofword = False


class ImplementTries():

    def __init__(self):
       self.root = Node()

    def insert(self, word):
        temp = self.root
        for letter in list(word):
            if letter not in temp.children:
                temp.children[letter] = Node()
            temp = temp.children[letter]
        temp.endofword = True
        # return self.root

    def search(self, word):
        temp = self.root
        for letter in list(word):
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        if temp.endofword :
            return True
        return False

    def starts_with(self, word):
        temp = self.root

        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return True









impl = ImplementTries()
impl.insert("word")
print(impl.search("word"))

impl.insert("wox")
print(impl.search("wox"))
print(impl.starts_with("wo"))
print(impl.search("word"))

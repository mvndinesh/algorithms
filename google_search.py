class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.lst =[]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        temp = self.root
        for each_letter in word:
            if each_letter not in temp.children:
                temp.children[each_letter] = TrieNode()
                temp.lst.append(word)
            temp = temp.children[each_letter]
            if word not in temp.lst:
                temp.lst.append(word)
        temp.end_of_word = True

    def return_suggestion(self,input_string):
        return_lst = None
        temp = self.root
        for each_letter in input_string:
            if each_letter in temp.children:
                temp = temp.children[each_letter]
                return_lst = temp.lst
            else:
                return return_lst
        return list(set(return_lst))


tri = Trie()
tri.insert("book")
tri.insert("bookstore")
tri.insert("bookman")
tri.insert("botman")
tri.insert("bottle")
print(tri.return_suggestion("book"))




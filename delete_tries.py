class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        temp = self.root
        for each_letter in word:
            if each_letter not in temp.children:
                temp.children[each_letter] = TrieNode()
            temp = temp.children[each_letter]
        temp.end_of_word = True

    def find_word(self, find_word):
        temp = self.root
        for each_letter in find_word:
            if each_letter not in temp.children:
                return False
            temp = temp.children[each_letter]
        if temp.end_of_word:
            return True
        return False

    def starts_with(self,starts_with):
        temp = self.root
        for each_letter in starts_with:
            if each_letter not in temp.children:
                return False
            temp = temp.children[each_letter]
        return True

obj_trie = Trie()
obj_trie.insert("dinesh")
print(obj_trie.find_word("dinesh"))
print(obj_trie.starts_with("din"))
obj_trie.insert("dog")
print(obj_trie.starts_with("do"))




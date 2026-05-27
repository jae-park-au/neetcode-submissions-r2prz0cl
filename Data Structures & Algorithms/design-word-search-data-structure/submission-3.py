class TrieNode:
    def __init__(self):
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        word = word + "$"

        for char in word:
            if char not in cur_node.children:
                next_node = TrieNode()
                cur_node.children[char] = next_node
                cur_node = next_node

            else:
                cur_node = cur_node.children[char]

    def search(self, word: str) -> bool:
        word = word + "$"
        
        return self.helpSearch(word, self.root, 0)

    def helpSearch(self, word: str, node: TrieNode, index: int) -> bool:
        for i in range(index, len(word)):
            char = word[i]

            if char == ".":
                for child in node.children.values():
                    if self.helpSearch(word, child, i + 1):
                        return True
                return False
            elif char in node.children:
                node = node.children[char]
            else:
                return False

        return True





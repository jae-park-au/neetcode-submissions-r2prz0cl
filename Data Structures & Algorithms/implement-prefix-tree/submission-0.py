class TrieNode:
    def __init__(self):
        self.child_nodes = {}

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root

        word = word + "$"
        for char in word:
            if char not in cur_node.child_nodes:
                next_node = TrieNode()
                cur_node.child_nodes[char] = next_node
                cur_node = next_node
            else:
                cur_node = cur_node.child_nodes[char]

    def search(self, word: str) -> bool:
        word = word + "$"

        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root

        for char in prefix:
            if char not in cur_node.child_nodes:
                return False
            else:
                cur_node = cur_node.child_nodes[char]
        
        return True
        
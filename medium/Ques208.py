# 208. Implement Trie (Prefix Tree)
# in python
class Trie:

    class Node:
        def __init__(self):
            self.child = [None] * 26
            self.eow = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            ind = ord(ch) - ord("a")

            if curr.child[ind] is None:
                curr.child[ind] = self.Node()

            curr = curr.child[ind]

        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            ind = ord(ch) - ord("a")

            if curr.child[ind] is None:
                return False

            curr = curr.child[ind]

        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            ind = ord(ch) - ord("a")

            if curr.child[ind] is None:
                return False

            curr = curr.child[ind]

        return True

# in java
class Trie {

    class Node {
        Node[] child = new Node[26];
        boolean eow = false;
    }

    Node root;

    public Trie() {
        root = new Node();
    }

    public void insert(String word) {
        Node curr = root;
        for (int i = 0; i < word.length(); i++) {
            int ind = word.charAt(i) - 'a';

            if (curr.child[ind] == null)
                curr.child[ind] = new Node();

            curr = curr.child[ind];
        }
        curr.eow = true;
    }

    public boolean search(String word) {
        Node curr = root;
        for (int i = 0; i < word.length(); i++) {
            int ind = word.charAt(i) - 'a';

            if (curr.child[ind] == null)
                return false;

            curr = curr.child[ind];
        }
        return curr.eow == true;
    }

    public boolean startsWith(String prefix) {
        Node curr = root;
        for (int i = 0; i < prefix.length(); i++) {
            int ind = prefix.charAt(i) - 'a';

            if (curr.child[ind] == null)
                return false;

            curr = curr.child[ind];
        }
        return true;
    }
}

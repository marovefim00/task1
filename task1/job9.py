class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    #узел древа
class BinarySearchTree:

    def __init__(self):
        self.root = None
    #бинарный поиск
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    #ищем и добавляем
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    #добовляем
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        return self._search(node.left, key) if key < node.key else self._search(node.right, key)
    #ищем
    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res
    #методы проходки(in-ord, pre-ord, post-ord)
    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)   # Лево
            res.append(node.key)            # Корень
            self._inorder(node.right, res)  # Право
    #in-ord(экей центрированный)
    def preorder(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, node, res):
        if node:
            res.append(node.key)            # Корень
            self._preorder(node.left, res)  # Лево
            self._preorder(node.right, res) # Право
    #pre-ord(экей прямой)
    def postorder(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, node, res):
        if node:
            self._postorder(node.left, res)  # Лево
            self._postorder(node.right, res) # Право
            res.append(node.key)             # Корень
    #post-ord(экей обратный)
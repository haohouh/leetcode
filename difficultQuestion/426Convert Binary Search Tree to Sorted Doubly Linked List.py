
class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return
        def dfs(root):
            if root == None: return
            dfs(root.left)
            if self.head == None:
                self.head = root
                self.tail = root
            else:
                self.tail.right = root
                root.left = self.tail
                self.tail = root
            dfs(root.right)
        dfs(root)
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head
        
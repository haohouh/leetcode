class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.index = 0
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def dfs(preorder,parentVal):
            if self.index == len(preorder) or preorder[self.index] > parentVal:
                return
            root = TreeNode(preorder[self.index])
            self.index += 1
            root.left = dfs(preorder,root.val)
            root.right = dfs(preorder,parentVal)
            return root
        return dfs(preorder,float("inf"))
        
                
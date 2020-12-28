class Solution(object):
    def __init__(self):
        self.curNode = None
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None: return
        def dfs(low,high):
            if low > high : return
            mid = low + (high - low) // 2
            l = dfs(low, mid - 1)
            root = TreeNode(self.curNode.val)
            root.left = l
            self.curNode = self.curNode.next
            root.right = dfs(mid + 1,high)
            return root      
        self.curNode = head
        l = 0
        cur = head
        while cur != None:
            cur = cur.next
            l += 1
        return dfs(0,l - 1)

"""
or

class Solution(object):
    def __init__(self):
        self.curNode = None
    
    def sortedListToBST(self, head):
        if head == None: return
        def dfs(low,high):
            if low > high : return
            mid = low + (high - low) // 2
            root = TreeNode(float("inf"))
            root.left = dfs(low, mid - 1)
            root.val = self.curNode.val
            self.curNode = self.curNode.next
            root.right = dfs(mid + 1,high)
            return root      
        self.curNode = head
        l = 0
        cur = head
        while cur != None:
            cur = cur.next
            l += 1
        return dfs(0,l - 1)
    
    
        


"""
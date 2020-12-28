class ListNode():
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None


def postOrder(root):
    if root == None: return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)

def postOrderNonRecu(root):
    if root == None: return
    stack = []
    res = []
    stack.append(root)
    while stack != []:
        cur = stack.pop()
        res.append(cur.val)
        if cur.left != None:
            stack.append(cur.left)
        if cur.right != None:
            stack.append(cur.right)
    for i in range(len(res)-1,-1,-1):
        print(res[i])




if __name__ == "__main__":
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(4)
    f = ListNode(5)
    g = ListNode(6)
    h = ListNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.left = f
    e.left = g
    e.right = h
    postOrder(a)
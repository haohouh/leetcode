class ListNode():
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None


def inOrder(root):
    if root == None: return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


def inOrderNonRecur(root):
    if root == None: return
    cur = root
    stack = []

    while stack != [] or cur != None:
        while cur != None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print(cur.val)
        cur = cur.right






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
    inOrderNonRecur(a)
class ListNode():
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

def preOrder(root):

    if root == None: return
    print (root.val)
    preOrder(root.left)
    preOrder(root.right)

def preOrderNonRecu1(root):
    if root == None: return
    stack = []
    stack.append(root)
    while stack != []:
        a = stack.pop()
        print (a.val)
        if a.right != None:
            stack.append(a.right)
        if a.left != None:
            stack.append(a.left)
    
def preOrderNonRecu2(root):
    if root == None: return
    stack = []
    cur = root
    while stack != [] or cur != None:
        while cur != None:
            stack.append(cur)
            print(cur.val)
            cur = cur.left
        cur = stack.pop()
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
    preOrderNonRecu2(a)













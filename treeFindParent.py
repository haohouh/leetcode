class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def Dfs(node,parent,parentMap,leafCollection,level,height):
    if node == None: return
    parentMap[node] = parent
    level[node] = height
    if node.left == None and node.right == None: leafCollection.append(node)

    Dfs(node.left,node,parentMap,leafCollection,level,height + 1)
    Dfs(node.right,node,parentMap,leafCollection,level,height + 1)



if __name__ == "__main__":
    a = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(6)
    h = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.left = f
    e.left = g
    e.right = h
    parentMap = {}
    level = {}
    leafCollection = []
    Dfs(a,None,parentMap,leafCollection,level,0)
    for key,value in parentMap.items():
        if value != None:
            print (key.val,value.val)
    for i in leafCollection:
        print (i.val)
    for key,value in level.items():
        print(key.val,value)
    


    
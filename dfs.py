'''
bfs , using stack
'''

def bfs(g,vertex):
    myQueue = []
    myQueue.append(vertex)
    seen = set(vertex)
    while len(myQueue)!= 0 :
        a = myQueue.pop()
        for i in g[a]:
            if i not in seen:
                seen.add(i)
                myQueue.append(i)
        print (a)
                



if __name__ == "__main__":
    g = {'A': ['B','C','D'],
         'B': ['A','C','D'],
         'C': ['A','B','D','F','E'],
         'D': ['A','B','C'],
         'E': ['C','F'],
         'F': ['C','G'],
         'G': ['F']
        }
    bfs(g,'A')
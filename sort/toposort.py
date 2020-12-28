def toposort(grpah):
    indegree = {key:0 for key in graph}   
    for _,j in graph.items():
        for m in j:
            indegree[m] += 1
    q = []

    for i,j in indegree.items():
        if j == 0: q.append(i)
    
    while q != []:
        m = q.pop(0)
        print (m)
        for next_node in graph[m]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)        










if __name__ == "__main__":
    graph = {1:[4,2],2:[3,4],3:[5],4:[3,5],5:[]}
    toposort(graph)   
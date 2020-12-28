def bfs(graph):
    #graph is adjenct list
    queue = []
    queue.append(graph[0])
    seen = set(graph[0])
    res = []
    while queue != []:
        cur = queue.pop(0)
        res.append(cur)
        for neighbor in cur:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return res
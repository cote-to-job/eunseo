from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]    
    distance = [-1] * (n+1)
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    #print(graph)
    queue =deque([1])
    distance[1]=0
    while queue:
        x = queue.popleft()
        #print(queue)
        for g in graph[x]:
            if distance[g] ==-1:
                distance[g] = distance[x]+1
                queue.append(g)
                
    #1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 
    for d in distance:
        if d == max(distance): answer+=1
    return answer
import sys
input =sys.stdin.readline

case_n = 1
while True:
    n, m = map(int,input().split() )
    
    #마지막 줄에는 0이 두 개
    if n == 0 and m == 0:
        break
    # 인접 리스트 초기화
    adj = [[] for _ in range(n+1)] #1부터 n까지 
    visit = [False] * (n+1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    tree_n = 0
    for i in range(1, n+1):
        if visit[i]:
            continue
        visit[i] = True
        isTree = True
        stack = [(i, -1)] #현재, 이전
        # DFS  
        while stack:
            cur, prev = stack.pop()
            for next in adj[cur]:
                if next == prev: # 1-2 == 2-1 로 
                    continue
                if visit[next]: #이미 방문 사이클 발생 
                    isTree = False
                    continue
                visit[next] = True
                stack.append((next, cur))
        tree_n += isTree
    
    
    if tree_n == 0:
        print(f"Case {case_n}: No trees.")
    elif tree_n == 1:
        print(f"Case {case_n}: There is one tree.")
    else:
        print(f"Case {case_n}: A forest of {tree_n} trees.")
    case_n += 1
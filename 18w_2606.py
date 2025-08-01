import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
pair = int(input())
warm = defaultdict(list)

for _ in range(pair):
    x,y = map(int,input().split())
    warm[x].append(y)
    warm[y].append(x)

visit = [0]*(n+1)
cnt =0
visit[1]=1
for k,v in warm.items():
    if visit[k]:
        for vv in v:
            visit[vv]=1
print(sum(visit))
def dfs(warm,visit,v):
    global cnt
    visit[v]=1
    for i in warm[v]:
        if not visit[i]:
            cnt+=1
            dfs(warm,visit,i)
    return cnt
#1번 바이러스 감염
print(dfs(warm,visit,1))



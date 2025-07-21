# 중간인 구슬이 될 수 없는 구슬의 개수를 구하는 프로그램을 작성
# 앞 번호의 구슬이 뒤 번호의 구슬보다 무겁다
from collections import deque
import sys
input = sys.stdin.readline

n,m= map(int,input().split())
light,heavy =[[] for _ in range(n+1)],[[] for _ in range(n+1)]
mid =(n+1)//2
for _ in range(m):
    h, l = map(int, input().split())
    heavy[h].append(l)
    light[l].append(h)

def bfs(li,bead):
    visit = [False]*(n+1)
    q= deque([bead])
    visit[bead] =True
    cnt =0
    
    while q:
        current = q.popleft()
        for next in li[current]:
            if not visit[next]:
                visit[next] = True
                q.append(next)
                cnt+=1
    if cnt >=mid:        return True
    else :return False
        
tot = 0
for i in range(1,n+1):
    if bfs(heavy,i) or bfs(light,i):       tot+=1
print(tot)

h[[], [], [1], [], [3, 2], [1]]

l[[], [2, 5], [4], [4], [], []]
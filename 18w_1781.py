import heapq
import sys 
input =sys.stdin.readline
n = int(input()) 
li=[tuple(map(int,input().split())) for _ in range(n)]
li.sort()
q = []
for i in li:
    heapq.heappush(q,i[1])
    if i[0] < len(q):
        heapq.heappop(q)
print(sum(q))
import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())

nli = [ list(map(int, input().split()))  for _ in range(n)]
kli = [int(input()) for _ in range(k)]

nli.sort()
kli.sort()

tmp=[]
max_val=0

for bag in kli:
    while nli and nli[0][0] <= bag:
        heapq.heappush(tmp, -nli[0][1])
        heapq.heappop(nli)#가장 무게 가벼운 것부터 삭제
    if tmp:
        max_val -= heapq.heappop(tmp)
print(max_val)


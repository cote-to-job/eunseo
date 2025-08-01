'''import sys
import heapq
input= sys.stdin.readline


for _ in range(n):
    x= int(input())
    if len(l) ==len(r):
        heapq.heappush(l,-x)
    else :
        heapq.heappush(r,x)
    if r and r[0] < -l[0]:
        lv,rv = heapq.heappop(l),heapq.heappop(r)
        
        heapq.heappush(l,-rv)
        heapq.heappush(r,-lv)
    print(-l[0])

'''

import sys, heapq

input = sys.stdin.readline
l = []
r = []

N = int(input())

center = int(input())
print(center)

for i in range(1, N):
    x = int(input())
    if x < center: # 중간보다 작은 값이면 왼쪽
        heapq.heappush(l, -x)
        if i%2 != 0: # 짝수 
            heapq.heappush(r, center)  
            center = -heapq.heappop(l)
    else:
        heapq.heappush(r, x)
        if i%2 == 0: # 홀수
            heapq.heappush(l, -center)
            center = heapq.heappop(r)
    print(center)

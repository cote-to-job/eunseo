'''
1->1
1,5 ->1
1,5,2 -> 2
1,5,2,10-> 2
1,5,2,10,-99->2
'''
import sys
import heapq
input= sys.stdin.readline

n = int(input())
l,r= [],[]

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

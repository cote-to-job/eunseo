import sys
input = sys.stdin.readline 
n,m = map(int, input().split())
A = [int(input()) for _ in range(n)]
A.sort()

answer = float("inf")

l, r = 0, 0

while r < n and l < n:
    diff = A[r] - A[l]
    
    if l == r:
        r += 1
        continue
    
    if diff < m:
        r += 1
    else :
        answer = min(answer, diff)
        l += 1
print(answer)

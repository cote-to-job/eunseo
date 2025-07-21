import sys
import heapq

input = sys.stdin.readline

N = int(input())
min_heap = []

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(min_heap) < N:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

print(min_heap[0])

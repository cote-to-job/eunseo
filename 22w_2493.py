import sys
input = sys.stdin.readline

n= int(input()) 

arr = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(len(arr)):

    while stack:
        if stack[-1][1] > arr[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
        
    stack.append((i,arr[i]))

print(*answer)
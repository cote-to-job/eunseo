import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    instr = input()
    if 'push' in instr:
        _,num =instr.split()
        q.append(num)
    elif 'pop' in instr:
        if q: print(q.popleft())
        else : print(-1)
    elif 'size' in instr:
        print(len(q))
    elif 'empty' in instr:
        if q: print(0)
        else: print(1)
    elif 'front' in instr:
        if q: print(q[0])
        else: print(-1)
    elif 'back' in instr:
        if q: print(q[-1])
        else: print(-1)





'''
import sys
from collections import deque
input =sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    order = input()
    
    if 'push' in order:
        _,num = order.split()
        q.append(num)
    
    elif 'pop' in order:
        if q: print(q.popleft())
        else:print(-1)
    elif 'size' in order:
        print(len(q))
    elif 'empty' in order:
        if q : print(0)
        else : print(1)
    elif 'front' in order:
        print(q[0] if q else -1)
    elif 'back':
        print(q[-1] if q else -1)'''
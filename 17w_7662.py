'''
정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. 
Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자.
Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 
최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.


'''
import sys
import heapq
from collections import deque

input = sys.stdin.readline

t= int(input())
# ‘I n’은 정수 n을 Q에 삽입
# ‘D 1’는 Q에서 최댓값을 삭제하는 
# ‘D -1’는 Q 에서 최솟값을 삭제하는 연산
#Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시
for i in range(t):
    numbers = int(input())
    q = []#deque()
    for j in range(numbers):
        x,n = input().split()
        n = int(n)
        if x == "I":
            heapq.heappush(q,n)
        elif x== "D" and n==1:
            if len(q) !=0:
                q.remove(max(q))
        else : 
            if len(q) !=0:
                heapq.heappop(q)
    if q :
        print(max(q), heapq.heappop(q))
    else:
        print("EMPTY")
'''1. 총에 1~n까지 총알이 있는 회전체 , 들어있으면 1 없으면 0, 1번시도(0) , 아직 발사는 안함
    
    총알이 아예 발사되지 않을 확률 구하기 
    
    ex) INPUT: [1,1,0,0,0,0] → RETURN: [1,2]
'''
from collections import deque
def solution(li,k):
    if 1 not in li: return [1,1]
    zero,one=0,0
    
    for i,x in enumerate(li):
        if x ==0:
            if 1 not in li[i:i+k]: zero+=1
            else: one+=1
            if 1 not in li[i-k:i] : zero+=1
            else : one+=1
    
    child = zero
    parent = zero+one

    for i in range(min(child,parent),0,-1):
        if child % i ==0 and parent %i==0:     
            return [child//i,parent//i]
            
            

li = [1,1,0,0,0,0] 
k = 2
#원형큐 사용




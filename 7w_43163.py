
#begin에서 target으로 변환해야하는데 words에 있는 단어로 
# 한 개씩 변환하면서 가장 짧은 변환 횟수 반환하기 
from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    visit = [True]*len(words)
    
    q.append([begin,0])
    while q:
        w,cnt =q.popleft()
        if w == target : return cnt
        for i,wd in enumerate(words):
            if visit[i]:#아직 방문X인 곳에서
                #한 글자 다른 단어 찾기
                tot =0
                for j in range(len(begin)):
                    if w[j] != wd[j] : tot+=1
                if tot ==1: 
                    visit[i] =False
                    q.append([wd,cnt+1])
                
        
    #변환할 수 없는 경우 
    return 0
solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

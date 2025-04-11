from collections import deque
def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]
    d = deque()
    while 0 in visit :
        d.append(visit.index(0))
        while len(d) !=0:
            now =d.popleft()
            for i in range(n):
                if computers[now][i] ==1 and visit[i]==0:
                    visit[i]=1
                    d.append(i)
        answer+=1
        
    # 네트워크의 개수
    return answer

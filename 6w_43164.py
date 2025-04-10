from collections import defaultdict
def solution(tickets): 
    #항상 "ICN" 공항에서 출발
    flight =["ICN"]
    route = defaultdict(list)
    for f,t in tickets:
        route[f].append(t)
    
    #가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 먼저
    for r in route:
        route[r].sort()
    
    answer =[]
    
    while flight:
        x = flight[-1]
        if route[x] !=[]:
            flight.append(route[x].pop(0))
        else :
            answer.append(flight.pop())
        
    
    #방문하는 공항 경로를 배열에 담아 return 
    return answer[::-1]
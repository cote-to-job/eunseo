def solution(n, costs):#n개의 섬 사이에 다리를 건설하는 비용(costs)
    answer = 0
    sort_cost = sorted(costs, key = lambda x: x[2])#비용 순으로 정렬

    #X = list(range(n + 1))

    X = set(range(n))# 0~n까지 set
    visit = set()
    visit.add(X.pop()) #0번 들어감
    while X:
        for i in range(len(sort_cost)):
            x1, x2, cost = sort_cost[i]
            if x1 in visit and x2 in visit: # 둘 다 존재 시 sort_cost는 앞이 더 낮은 값으로 제거
                sort_cost.pop(i)
                break
            elif x1 in visit or x2 in visit:
                if x1 in X:#x1에 존재 시 제거(앞 값 더 cheap)
                    X.remove(x1)
                if x2 in X:
                    X.remove(x2)
                #방문 경로 넣고 
                visit.add(x1)
                visit.add(x2)
                #cost에 더한 후 
                answer += cost
                # 값 제거
                sort_cost.pop(i)
                break

    return answer
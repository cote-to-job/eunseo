def solution(routes):
    # 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return
    #routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점
    
    routes.sort(key=lambda x: x[1])
    #[-20, -15], [-18, -13] -18~-15, [-14, -5], [-5, -3] -5 ,[2,4],[1,5] 234

    cam = 0
    out = -30001  
    for start, exit in sorted(routes, key=lambda item: item[1]):

        if out < start:
            cam += 1
            out = exit   
    
    return cam 
'''
    for i in range(len(r)-1):
        if r[i+1][0] <= r[i][1]:
            answer.append([max(r[i][0],r[i+1][0]),min(r[i][1],r[i+1][1])])
    cam_spot = sorted({seg[1] for seg in answer})
'''
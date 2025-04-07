def solution(jobs):
    answer = 0
    now = 0          # 현재 시간
    total = 0        # 반환 시간 합
    size = len(jobs) #  작업 개수

    # 모든 작업을 처리할 때까지 
    while len(jobs) > 0:
        min_time = 10000000  
        index = len(jobs)    
        
        # now까지 요청된 작업 중 소요시간이 가장 짧은거
        for schedule in jobs:
            if schedule[0] <= now and min_time > schedule[1]:
                min_time = schedule[1]
                index = jobs.index(schedule)
                
        # 처리 가능한 작업
        if index != len(jobs):
            # 반환 시간 계산: now - 요청 시각 + 작업 소요시간
            total += min_time + now - jobs[index][0]
            now += jobs[index][1]  # 현재 시각 업데이트
            jobs.pop(index)        # 작업 제거
        else:
            now += 1  # 현재 시각에 처리 가능한 작업이 없으면 1ms씩 증가


    answer += total // size
    return answer

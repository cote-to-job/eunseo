'''def solution(diffs, times, limit):
    answer, left, right = 0, 1, 100000 #1 ≤ diffs[i] ≤ 100,000 
    #현재퍼즐 -time_cur , 이전퍼즐 -time_prev

    while left <= right:
        level = (left + right) // 2
        total_time = 0

        for i, _ in enumerate(diffs):
            if diffs[i] <= level:    #diff ≤ level 이면 시간을 time_cur 만큼만 사용

                total_time += times[i]
            else:
                #diff > level 이면 퍼즐을 diff-level번 틀림 + time_cur만큼 시간 사용 + (+timeprev 시간걸림)+time_cur 사용

                #틀린개수* (time_pre+time_cur)+time_cur
                total_time += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
        # 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 정수로 return 
        if total_time > limit: left = level + 1
        else: answer, right = level, level - 1

    return answer

'''
def puzzle(diffs, times, limit, level):
    clear_time = 0
    for idx in range(len(diffs)):
        if diffs[idx] <= level: 
            clear_time += times[idx]
        elif diffs[idx] > level: 
            clear_time += (diffs[idx]-level)*(times[idx-1]+times[idx])+times[idx]
        if clear_time > limit: 
            return False
    return True
 
def solution(diffs, times, limit):
    start, mid, end = 1,0,max(diffs)
 
    while start<=end:
        mid = (start+end)//2
        
        if puzzle(diffs, times, limit, mid): 
            end = mid-1
        else: 
            start = mid+1
    
    ## start : 1, mid : 1, end : 2 인 경우
    if puzzle(diffs, times, limit, mid): 
        return mid
    if puzzle(diffs, times, limit, mid+1): 
        return mid+1
    
    return mid-1

solution([1, 5, 3],	[2, 4, 7]	,30)
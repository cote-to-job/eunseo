#출근 희망 시각 + 10분까지 출근
def solution(schedules, timelogs, startday):
    answer = 0
    li=[]
    for i,s in enumerate(schedules):
        hour = s//100
        minute = s %100
        access = minute +10
        if  access>=60:
            access %=60
            hour +=1    
        goto= hour*100+access
        
        late= False
        day = startday
        for j in range(7):
            if day in (6,7) :pass
             
                
            else: 
                if goto < timelogs[i][j] : 
                    late =True
                    print(goto,timelogs[i][j])
            if day <7:
                day+=1
            else: day=1
        if not late:
            answer+=1
            
    return answer 
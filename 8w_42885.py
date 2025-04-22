# 50,50,70,80 
# 대칭으로 구하면 50+80 X 50+70X 50+50 O
def solution(people, limit):
    answer = 0
    people.sort()
    light ,heavy = 0, len(people)-1
    num_boat=0
    
    while light <=heavy: # 50 <=50
        if people[light] + people[heavy] <=limit: 
            light+=1
        heavy -=1 #더 낮은 값으로 만들면서 계산 
        num_boat+=1
    
    
    
    return num_boat
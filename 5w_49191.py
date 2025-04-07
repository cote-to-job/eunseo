#A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이김
#정확하게 순위를 매길 수 있는 선수의 수return
def solution(n, results):
    answer = 0
    win, lose = {}, {}

    
    for winner, loser in results:
        if loser not in win:
            win[loser] = set()
        win[loser].add(winner) #win = { 3: {4}, 2: {4} }


        if winner not in lose:
            lose[winner] = set()
        lose[winner].add(loser) #lose = { 4: {2, 3} }

    
    for i in range(1, n + 1):
        # [x, i] -> [i, a ] 존재 시 win[x]에 a도 추가
        for winner in win.get(i, set()):
            if winner not in lose:
                lose[winner] = set()
            lose[winner].update(lose.get(i, set()))
        
        # 위와 반대
        for loser in lose.get(i, set()):
            if loser not in win:
                win[loser] = set()
            win[loser].update(win.get(i, set()))

    #  정확한 순위의 선수 수 
    for i in range(1, n + 1):
        if len(win.get(i, set())) + len(lose.get(i, set())) == n - 1:
            answer += 1

    return answer


    
'''
    4>3 
    4>2
    3>2
    1>2
    2>5
    2>5 명확
    4>3>2이지만 1 위치 미지수
'''

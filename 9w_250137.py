def solution(bandage, hp, attacks):
    #1초씩 x 만큼 회복 & t초 동안 y만큼 추가적 회복
    #시전 시간, 1초당 회복량, 추가 회복량 : bandage
    #최대 체력 : health, 몬스터의 공격 시간과 피해량: 2차원 attacks
    # 2초에 공격 damange:10 hp -> 20, 3~8초 동안 x만큼회복 +5초로 y만큼 회복 
    #9초에 공격 hp-15
    answer = 0
    t,x,y= bandage
    seq =0
    max_hp =hp
    sf= attacks[:-1]
    for i,(a_t,a_d) in enumerate(attacks[:-1]):
        hp -= a_d
        
        if hp <=0 :
            return -1
        # 붕대
        if i < len(attacks) - 1:
            next_time = attacks[i+1][0]
            sec = next_time - a_t - 1  
            if sec > 0:
                heal = x * sec + (sec // t) * y
                hp = min(hp + heal, max_hp)
    return hp
solution([3, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]])
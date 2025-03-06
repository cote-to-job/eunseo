# 목표: c에 없는 사람 return
def solution(participant, completion): #p:참여자, c: 완주자
    participant.sort()
    completion.sort()
    len(participant)
    for p,c in zip(participant, completion):
        if p != c: 
            return p
    return participant[-1]
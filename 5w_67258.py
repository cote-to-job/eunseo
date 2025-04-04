#진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

def solution(gems):
    kind = len(set(gems)) 
    answer = [0, len(gems) - 1] #시작~끝
    
    dic = {gems[0]:1}
    start ,end = 0 ,0 #end를 0부터 시작해서 끝까지 탐색
    while end < len(gems):
        if len(dic) < kind: #전체 종류랑 dic이랑 같게 만들기
            end += 1
            if end == len(gems): break
            dic[gems[end]] = dic.get(gems[end], 0) + 1 
        else:##전체 종류랑 dic이랑 같을 때 
            if (end - start + 1) < (answer[1] - answer[0] + 1): answer = [start, end]
            if dic[gems[start]] == 1: del dic[gems[start]]
            else: dic[gems[start]] -= 1
            start += 1

    answer[0] += 1
    answer[1] += 1
    # 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return
    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
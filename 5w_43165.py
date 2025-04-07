def solution(numbers, target):# 숫자가 담긴 배열 numbers, 타겟 넘버 target
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []#tmp에 더하거나 뺀 수를 저장
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    #타겟 넘버를 만드는 방법의 수를 return 
    return answer
solution([4, 1, 2, 1],3)
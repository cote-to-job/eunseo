'''시간초과
# k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
def solution(number, k):
    nums     = list(number)
    tot        = len(nums)
    result   = []
    start    = 0

    for i in range(tot-k):# k개 제거
        end = k+i 
        window    = nums[start : end+1]
        max_num = max(window)
        idx       = nums.index(max_num, start, end+1)

        result.append(max_num)

        start = idx + 1

    return ''.join(result)
'''
def solution(number, k):
    answer = []
    
    if len(set(number))==1: # 1개 숫자만 존재 시 처리리
        return number[k:]
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    
    return ''.join(answer[:len(answer)-k])#number의 숫자가 만약 큰 순서대로 되어있다면 처음~끝-k로 처리리


solution("333222111 ",3)
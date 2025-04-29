def NToTen(n, num):
    if len(num)==1: return int(num)
 
    number = 0
    for idx in range(len(num)):
        number += int(num[idx])*(n**(len(num)-1-idx))
 
    return number
 
def TenToN(n, num):
    if num==0: return "0"
    answer = ""
 
    for idx in range(2,-1,-1):
        div = num // (n**idx)
        if answer or div: answer += str(div)
        num = num % (n**idx)
 
    return answer
 
def solution(expressions):
    answer, answer_format = [], []
    max_format, hint = 0, []
    for e in expressions:
        num1, func, num2, _, ans = e.split(" ")
        
        for idx in range(len(num1)): max_format = max(max_format, int(num1[idx]))
        for idx in range(len(num2)): max_format = max(max_format, int(num2[idx]))
        
        if ans != "X": 
            hint.append(e)
            for idx in range(len(ans)): max_format = max(max_format, int(ans[idx]))
        else: answer.append(e)
    
    for n in range(max_format+1, 10):
        check = 1
        for h in hint:
            num1, func, num2, _, ans = h.split(" ")
            num1, num2, ans = NToTen(n, num1), NToTen(n, num2), NToTen(n, ans)
            if (func == '+') and (num1+num2!=ans): 
                check = 0
                break
            if (func == '-') and (num1-num2!=ans): 
                check = 0
                break
        
        if check: 
            answer_format.append(n)
    
    for idx in range(len(answer)):
        num1, func, num2, _, ans = answer[idx].split(" ")
        ans_set = set()
        for a in answer_format:
            num_1, num_2 = NToTen(a, num1), NToTen(a, num2)
 
            if func=="+": ans_set.add(str(TenToN(a, num_1+num_2)))
            if func=="-": ans_set.add(str(TenToN(a, num_1-num_2)))
        
        if len(ans_set)==1:
            answer[idx] = ' '.join([num1, func, num2, _, list(ans_set)[0]])
        else: answer[idx] = ' '.join([num1, func, num2, _, "?"])
            
    return answer

'''
2~9진법
?*1+4 +3 = ?*1+7   
?*5+1 -5 =?*4 +4 -> ?*1 -4 = +4  ? = 8
8*1+3 - 6 =5

1+1 =2
1+3 =4 
-> 2~4진법X
1+2 = 3
1+5 = 모름 so, ?로대체

?*3+1+ ?*3 = ?*6 = 10 -> 6진법

2-1 =1
2+2 =X =?
7+4 =X =?
5-5 = X =0


2-1 =1
2+2 =X
7+4 =X 
8+4 =X
인데 2,7,8이 10형태로 쓰이지 않고 숫자로 작성되어있으므로 남은 하나의 숫자인 9'''
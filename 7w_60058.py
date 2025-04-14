def solution(p):
    # 1. 빈 문자열이면 빈 문자열로 반환
    if p == '': return p
    is_p = True
    parentheses = 0
    
    for i in range(len(p)):
        if p[i] == '(': parentheses -= 1
        else : parentheses += 1
        # ) 먼저 나온 경우 처리 
        if parentheses > 0: is_p = False
        #균형잡힌 괄호 문자열이면 +-로 0 나옴 & u,v로 나누기
        if parentheses == 0 :
            # i번째 일 때 만족하므로 0~i까지 | i+1 ~로 
            u = p[:i+1] 
            v= p[i+1:]
            if is_p :# ( 먼저나온 경우 
                # u가 온전한 괄호로 u까지는 검증 완
                return u +solution(v)
            else :# ) 가 먼저 나온 경우 
                reverse = ''
                for c in u[1:-1]:#양 끝은 () 로 바꿔야하므로 제외
                    #역으로 바꿔서 문제 해결
                    if c =="(" : reverse +=')'
                    else : reverse +='('
                    
                return '('+ solution(v) +')'+reverse
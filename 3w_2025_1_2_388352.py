from itertools import combinations
def solution(n, q, ans):
    answer = 0
    sol = [i for i in range(1,n+1) ]
    #ans가 0일때 모두 제거
    if 0 in ans:
        for i,a in enumerate(ans):
            if a==0:
                sol = [x for x in sol if x not in q[i]]
                #del q[i]
                print(q)
    all_combi = list(combinations(sol,5))
    for candidate in all_combi:
        is_valid = True
        for i in range(len(q)):
            ex_count = ans[i]
            act_count = len(set(candidate) & set(q[i]))
            if act_count != ex_count:
                is_valid = False
                break
        if is_valid :
            answer+=1
            
    return answer
n = 15
q = [
    [2, 3, 9, 12, 13],
    [1, 4, 6, 7, 9],
    [1, 2, 8, 10, 12],
    [6, 7, 11, 13, 15],
    [1, 4, 10, 11, 14]
]
ans = [2, 1, 3, 0, 1]

solution(n, q, ans)
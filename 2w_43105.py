
#  거쳐간 숫자의 합이 가장 큰 경우

def solution(triangle):
    line= len(triangle)
    max_ans =0
    for i in range(line-1, -1, -1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j:j+2])
    return triangle[0][0]
            
            
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	)
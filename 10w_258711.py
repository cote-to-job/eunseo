#    도넛 모양 , 막대 모양 , 8자 모양 
#정점   n개        n개       2n+1개
#간선   n개        n-1개     2n+2개
def solution(edges):  
    answer = [0, 0, 0, 0]  # 생성 정점 번호, 도넛 그래프 수, 막대 그래프 수, 8자 그래프 수
    edge_counts = {}

    for out, to in edges:
        # 각 노드별 간선 수 딕셔너리 생성
        if not edge_counts.get(out):       edge_counts[out] = [0, 0]
        if not edge_counts.get(to):        edge_counts[to] = [0, 0]

        # output edge와 input edge 개수 추가
        edge_counts[out][0] += 1  # 나가는 간선 수
        edge_counts[to][1] += 1   # 들어오는 간선 수

    max_value = max(max(e) for e in edges)
    
    for key, counts in edge_counts.items():
        # 생성 정점 (나가는 간선 2개 이상, 들어오는 간선 없음)
        if counts[0] >= 2 and counts[1] == 0:
            answer[0] = key
        # 막대 그래프 끝점 (나가는 간선 없고, 들어오는 간선 있음)
        elif counts[0] == 0 and counts[1] > 0:
            answer[2] += 1
        # 8자 그래프 중앙점 (들어오는 간선과 나가는 간선 모두 2개 이상)
        elif counts[0] >= 2 and counts[1] >= 2:
            answer[3] += 1

    # 도넛 그래프 수 = 생성된 정점에서 나간 간선 수 - 막대 수 - 8자 수
    answer[1] = edge_counts[answer[0]][0] - answer[2] - answer[3]

    return answer

solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])
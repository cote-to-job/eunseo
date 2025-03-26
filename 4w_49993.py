#무조건 skill 순서대로만 해야함 
#skill_tree에서 skill순서에 맞게 구성 시 return +=1
def solution(skill, skill_trees):
    answer = 0
    skill_order = [i for i in skill]
    #skill 을 제외하고 다 제거
    for leaf in skill_trees:
        order =[]#order에 스킬에 맞는 것만 들어가게 설계
        for leaf_skill in leaf:
            if leaf_skill in skill:
                order.append(leaf_skill) 
        if order == skill_order[:len(order)]:#순서가 중요하고 길이는 order만큼
            answer+=1
    return answer
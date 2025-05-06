#기록 존재 시 이번달 up -> +1
#기록 X시 선물지수가 큰사람 +1
#선물지수 : 준 선물-받은 선물
def solution(friends, gifts):
    f=len(friends)
    giveget = [[0]*f for _ in range(f)]
    nextM = [0]*f
    name_dict = {name: index for index, name in enumerate(friends)}
    for i in gifts:
        a= i.find(' ') 
        giveget[name_dict[i[:a]]][name_dict[i[a+1:]]]+=1
    gividx = [sum(row) - sum(col) for row, col in zip(giveget, zip(*giveget))]

    for i in range(f):
        for j in range(f):
            if i ==j : continue
            if giveget[i][j] >giveget[j][i]:
                nextM[i]+=1
            elif giveget[i][j] == giveget[j][i]:
                if gividx[i]>gividx[j]:       nextM[i]+=1 
    
    #다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return
    return max(nextM)
solution(	["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])
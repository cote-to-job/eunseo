#진도가 100%일 때 서비스에 반영 &뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
def solution(progresses, speeds):
    answer = []
    
    for p,s in zip(progresses,speeds):
        left = -(p-100)//s
        if not answer or answer[-1][0]<left:
            answer.append([left,1])
        else: answer[-1][1]+=1
    return [a[1] for a in answer]
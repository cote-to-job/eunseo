def solution(name):
    answer = 0
    #위 - 다음 , 아래 - 이전 알파벳
    move = [0]*len(name)
    for i,n in enumerate(name):
        up = ord(n)- ord('A')
        down = ord('Z') - ord(n)+1
        move[i]=min(abs(up),abs(down))
        #if move[i] ==0 and i==1: 
        #    move[i]+=1 JAN에서  다음 문자 A->왼쪽 +1해서 마지막으로
    #JEROEN 51... 
    #좌 - 왼쪽이동, 우- 오른쪽이동
    #좌 -  첫번째 위치면 맨 마지막 문자로 , 우 - 마지막 위치면 첫 번째 문자로
    n=len(name) #AAAA일때
    lr = n-1 #☑️ 1. 그냥 오른쪽으로 쭉
    for i in range(n):
        next = i+1 
        while next <n and name[next]=='A': #마지막 문자가 아니고, next가 A일 때
            next +=1 # 옆으로 이동만 있으므로 +1   
            d1 = 2*i +(n-next) #우 R ☑️ 2. 오른쪽으로 갔다가 돌아서 왼쪽으로 가기
            d2 = i+2*(n-next) #좌 L AAAJ :idx=0 -> 마지막idx +1  3. 왼쪽으로 돌아서 갔다가 오른쪽으로 쭉
            lr = min(lr,d1,d2)
    
    answer = sum(move) + lr
    return answer

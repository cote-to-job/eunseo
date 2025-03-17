#n:택배 상자의 개수 w: 가로로 놓는 상자의 개수 num:상자번호 
#꺼내야 하는 상자의 총개수를 return 
'''
def solution(n, w, num):
    box=1
    li=[0]*w
    i = num//w
    line =n//w 
    left = n%w
    if left ==0:
        return line -i
    if line%2 : 
        li[w - left:] = [1] * left    
        
    else: 
        li[:left] = [1] * left  
        
        print(num %w)
    
        


'''
#n:택배 상자의 개수 w: 가로로 놓는 상자의 개수 num:상자번호 
#꺼내야 하는 상자의 총개수를 return 
'''
def solution(n, w, num):
    box=1
    li=[0]*w
    i = num//w
    line =n//w 
    left = n%w
    if left ==0:
        return line -i
    if line%2 : 
        li[w - left:] = [1] * left    
        
    else: 
        li[:left] = [1] * left  
        
        print(num %w)
    
        


'''
def solution(n, w, num):
    box=1
    li=[]
    
    for i in range(n//w+1):
        if i % 2 :#홀수줄            
            box_list=list(range(min(box+w,n),box-1,-1 ))
        
            print(box_list)
        else:#짝수줄
            box_list=list(range(box, min(box+w,n+1)))
            print(box_list)
        box +=w
        li.append(box_list)
    
    for i, row in enumerate(li):
        if num in row:
            j = row.index(num)
            print(len(li),i,j)
            answer = len(li)-i
            break
            
                    
    return answer

solution(22,	6,	8)
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = h1*3600+m1*60+s1
    end   = h2*3600+m2*60+s2
    answer+=int(end/3600*59)
    answer-=start//(3600/59)
    answer+=end//(360*120/719)
    answer-=start//(360*120/719)
    if start<=12*60*60<=end:answer-=1
    if start==0 or start==12*60*60:answer+=1

    return answer
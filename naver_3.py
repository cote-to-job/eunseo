'''완탐? 과일 종류 n개, 각 과일은 m가지 맛을 가지고 있음
과일 n개 중 k개 선택해서 과일 맛 조합 생성, 생성된 과일맛 같으면 1, 과일 맛 조합 구하기'''
from itertools import combinations

def solution(fruits,k):
    max_taste = 1*len(fruits[0])
    li = []
    for f in fruits:
        value = int(f,2) #2->10로 변환
        li.append(value) #10진수 버전으로 저장
    
    result = set() #중복 1취급하므로 set사용
    combi_fruit = combinations(li,k) #k개 사용 시 조합
    for c in combi_fruit:
        combi =0
        for x in c:
            combi = combi | x # OR연산으로 맛 합치기기
        result.add(combi)
    return len(result)
    
fruits = ['1000','0110','0001','1000']#["100","001","011"] #["1000","1011","1100","0101"]
k = 2
solution(fruits,k)


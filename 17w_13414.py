import sys
input = sys.stdin.readline

k, l = map(int, input().split())

# 수강신청 정보를 저장할 딕셔너리 (학번: 신청순서)
signup = {}

for i in range(l):
    stu_num = input().strip()
    signup[stu_num] = i  # 마지막 신청 순서만 저장

slist = list(signup.items())

# 신청순서 기준
slist.sort(key=lambda x: x[1])

# 최대 k명
k = min(k, len(slist))

for i in range(k):
    print(slist[i][0])
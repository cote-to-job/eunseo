# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c

from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr += arr[:k-1]  # 회전 초밥이므로 앞부분을 뒤에 추가

window = defaultdict(int)
window[c] += 1  # 쿠폰 초밥 미리 추가

# 초기 윈도우 설정
for i in range(k):
    window[arr[i]] += 1

max_sushi = len(window)

# 슬라이딩 윈도우
left = 0
for right in range(k, n + k - 1):  # 슬라이딩 범위: n번 이동
    window[arr[right]] += 1
    window[arr[left]] -= 1
    if window[arr[left]] == 0:
        del window[arr[left]]
    left += 1
    max_sushi = max(max_sushi, len(window))

print(max_sushi)

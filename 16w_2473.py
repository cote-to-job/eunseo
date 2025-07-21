'''
산성 : 1~ 10**9
알칼리성 : -1 ~ -10**9
0에 가장 가까운 용액을 만들려고 한다. 

예를 들어, 주어진 용액들의 특성값이 [-2, 6, -97, -6, 98]인 경우에는 특성값이 -97와 -2인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 
참고로, 세 종류의 알칼리성 용액만으로나 혹은 세 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
'''
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    arr.sort()
    
    # 초기값 설정 (첫 번째 삼중항)
    best_sum = abs(arr[0] + arr[1] + arr[2])
    best_triple = [arr[0], arr[1], arr[2]]
    
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if abs(s) < best_sum:
                best_sum = abs(s)
                best_triple = [arr[i], arr[left], arr[right]]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:  # 합이 0이면 즉시 내부 루프 종료
                break
                
    best_triple.sort()
    print(f"{best_triple[0]} {best_triple[1]} {best_triple[2]}")

if __name__ == "__main__":
    main()

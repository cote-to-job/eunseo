import sys
import heapq

def isEmpty(nums):
    for n in nums:
        if n[1]> 0: return False
    return True

input = sys.stdin.readline

t = int(input())

for i in range(t):
    minH,maxH =[],[]
    nums = dict()
    k = int(input())

    for _ in range(k):
        '''
        1. ‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 동일한 정수가 삽입될 수 있음을 참고하기 바란다.
        2. ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며,
        3. ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다. 
        '''
        chr,n =input().split()
        n = int(n)

        if chr =='I':
            if n in nums : nums[n]+=1
            else: 
                nums[n] =1
                heapq.heappush(minH,n)
                
                heapq.heappush(maxH,-n)
        elif chr =='D':
            if not isEmpty(nums.items()):
                if n==1:
                    while -maxH[0] not in nums  or nums[-maxH[0]] <1:
                        #
                        temp = -heapq.heappop(maxH)
                        if temp in nums:
                            del(nums[temp])
                    nums[-maxH[0]] -=1
                else:
                    while minH[0] not in nums or nums[minH[0]] <1:
                        temp = heapq.heappop(minH)
                        if temp in nums: del(nums[temp])
                        nums[minH[0]] =1
            

    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while minH[0] not in nums or nums[minH[0]] < 1:
            heapq.heappop(minH)
        while -maxH[0] not in nums or nums[-maxH[0]] < 1:
            heapq.heappop(maxH)
        print(-maxH[0], minH[0])
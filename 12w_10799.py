s = input().strip()
stack = []
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if i > 0 and s[i-1] == '(':  # 레이저인 경우
            ans += len(stack)
        else:  # 막대 끝인 경우
            ans += 1

print(ans)

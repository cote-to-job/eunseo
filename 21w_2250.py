import sys
sys.setrecursionlimit(10000)

MXN = 10010
lc = [-1] * MXN
rc = [-1] * MXN
colLR = [[0, 0] for _ in range(MXN)]

N = int(sys.stdin.readline())
is_root = [True] * (N + 1)

for _ in range(N):
    p, l, r = map(int, sys.stdin.readline().split())
    lc[p] = l
    rc[p] = r
    if l != -1:
        is_root[l] = False
    if r != -1:
        is_root[r] = False

# 루트 찾기
for i in range(1, N + 1):
    if is_root[i]:
        root = i
        break

colno = 0
def inorder(curr, d):
    global colno
    if curr == -1:
        return
    inorder(lc[curr], d + 1)
    colno += 1
    lcol, rcol = colLR[d]
    if lcol == 0 or colno < lcol:
        colLR[d][0] = colno
    if rcol == 0 or rcol < colno:
        colLR[d][1] = colno
    inorder(rc[curr], d + 1)

inorder(1, 0)

mx_width = 0
mx_depth = 0
for d in range(N):
    lcol, rcol = colLR[d]
    if lcol + rcol == 0:
        break
    width = rcol - lcol + 1
    if width > mx_width:
        mx_width = width
        mx_depth = d

print(mx_depth + 1, mx_width)

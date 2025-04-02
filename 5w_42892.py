import sys
#nodeinfo의 길이는 1 이상 10,000 이하
sys.setrecursionlimit(10000)

def solution(nodeinfo):
    # 1. 각 노드에 고유 번호(1부터 시작)를 부여하고, 좌표와 함께 저장
    # nodes = [(x좌표, y좌표, 노드번호)]
    nodes = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]

    # 2. y 기준 내림차순 → 같은 y일 경우 x 기준 오름차순으로 정렬
    # => 가장 위에 있는 노드가 루트가 되며, 같은 level이면 x값에 따라 좌우 결정
    nodes.sort(key=lambda x: (-x[1], x[0]))

    # 3. 트리 구성용 클래스 정의
    class Node:
        def __init__(self, x, y, idx):
            self.x = x          # x좌표
            self.y = y          # y좌표
            self.idx = idx      # 노드 번호
            self.left = None    # 왼쪽 자식 노드
            self.right = None   # 오른쪽 자식 노드

    # 4. 트리에 노드를 삽입하는 함수 정의 (이진 탐색 트리 규칙에 따라)
    def insert(parent, child):
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                insert(parent.left, child)
        else:
            if parent.right is None:
                parent.right = child
            else:
                insert(parent.right, child)

    # 5. 첫 번째 노드를 루트로 설정
    root = Node(*nodes[0])

    # 6. 나머지 노드를 트리에 삽입
    for node in nodes[1:]:
        insert(root, Node(*node))

    # 7. 전위 순회 결과 저장용 리스트
    preorder_result = []

    # 8. 후위 순회 결과 저장용 리스트
    postorder_result = []

    # 9. 전위 순회: 루트 → 왼쪽 → 오른쪽
    def preorder(node):
        if node:
            preorder_result.append(node.idx)  # 루트 처리
            preorder(node.left)               # 왼쪽 서브트리
            preorder(node.right)              # 오른쪽 서브트리

    # 10. 후위 순회: 왼쪽 → 오른쪽 → 루트
    def postorder(node):
        if node:
            postorder(node.left)              # 왼쪽 서브트리
            postorder(node.right)             # 오른쪽 서브트리
            postorder_result.append(node.idx) # 루트 처리

    # 11. 순회 실행
    preorder(root)
    postorder(root)

    # 12. 결과 반환: [전위 순회 결과, 후위 순회 결과]
    return [preorder_result, postorder_result]

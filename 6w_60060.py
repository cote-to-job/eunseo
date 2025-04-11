'''
단어 길이 & ? 제외한 단어 모두 일치해야 함
검색 키워드는 접두사 또는 접미사 형태로만 와일드카드(?)가 등장하므로
앞에서부터 매칭하거나 뒤에서부터 매칭하는 방식으로 구분 가능함.
Trie 자료구조를 이용하여 빠르게 단어의 접두사/접미사 패턴 매칭을 수행함.
'''

# Trie를 구성하는 노드 클래스 정의
class Node(object):
    def __init__(self, key):
        self.key = key            # 해당 노드가 가지는 문자
        self.count = 0            # 해당 노드를 거쳐간 단어의 개수
        self.children = {}        # 다음 문자 노드들 (딕셔너리)

# Trie 자료구조 정의
class Trie(object):
    def __init__(self):
        self.head = Node(self)

    def insert(self, string):
        current = self.head
        for char in string:
            current.count += 1  # 해당 노드를 거쳐감 = 카운트 증가
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

    def starts_with(self, prefix):
        '''
        주어진 prefix(패턴)로 시작하는 단어가 몇 개인지 반환
        '?'가 나오는 시점까지만 탐색하면 되며,
        중간에 매칭되지 않으면 0 반환
        '''
        current = self.head
        result = 0

        for char in prefix:
            if char == '?':  # 와일드카드 도달 시 탐색 중단
                break
            if char in current.children:
                current = current.children[char]
            else:
                return 0  # 매칭 불가능한 문자 포함

        return current.count  # 해당 prefix까지 도달한 단어 수

def solution(words, queries):
    answer = []
    tries = {}          # 정방향 Trie (단어 그대로)
    reverse_tries = {}  # 역방향 Trie (단어를 뒤집은 형태)

    # 단어들을 Trie에 삽입 (길이별로 구분하여 저장)
    for word in words:
        size = len(word)
        if size not in tries:
            tries[size] = Trie()
            reverse_tries[size] = Trie()
            
        tries[size].insert(word)
        reverse_tries[size].insert(word[::-1])  # 접미사 패턴용 역방향 저장

    # 각 쿼리에 대해 매칭되는 단어 수 계산
    for query in queries:
        q_len = len(query)
        if q_len not in tries:
            answer.append(0)  # 해당 길이의 단어가 아예 없음
            continue

        # 접두사 패턴 (fro?? 같은 경우)
        if query[0] != '?':
            trie = tries[q_len]  # 정방향 Trie 사용
            answer.append(trie.starts_with(query))
        else:
            # 접미사 패턴 (??odo 같은 경우)
            trie = reverse_tries[q_len]  # 역방향 Trie 사용
            answer.append(trie.starts_with(query[::-1]))

    return answer

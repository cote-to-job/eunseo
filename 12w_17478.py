'''
재귀함수 출력 
형식
?
ㅁ
___ㅁ
______ㅁ
---------재귀함수?
______ans
___ans
ans
'''
def bot(n, cnt):
    t="____"
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    print(t * cnt + '"재귀함수가 뭔가요?"')

    if cnt == n:
        print(t * cnt + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(t * cnt + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(t * cnt + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(t * cnt + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        bot(n, cnt + 1)
    print(t* cnt + "라고 답변하였지.")


n = int(input())

bot(n, 0)



start = ('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n'
        +'"재귀함수가 뭔가요?"\n')

recursion1 =['"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n',
        '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n',
        '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n']
define =['"재귀함수가 뭔가요?"\n','"재귀함수는 자기 자신을 호출하는 함수라네"\n']
recursion2 = '라고 답변하였지.\n'


n = int(input())
t = '____'

print_ans = [start]
fin = []
for i in range(n+1):
    strp =t*i
    if i ==n+1 :
        print_ans.append(t*i+define)
        
        break
    print_ans.append((t*i)*recursion1)
    fin.append((n-i)*t+recursion2)
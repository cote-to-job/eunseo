#list[x]이 list[y]의 
#접두어 O면 false를 접두어 X면 true를 return
def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx,phone in enumerate(phone_book[:-1]):
        if phone == phone_book[idx+1][:len(phone)]:
            return False
    
    return answer
def solution(phone_book):
    phone_book.sort()
    
    for j in range(len(phone_book)-1):
        N = len(phone_book[j])
        if phone_book[j+1][:N] == phone_book[j]:
            return False
    
    return True
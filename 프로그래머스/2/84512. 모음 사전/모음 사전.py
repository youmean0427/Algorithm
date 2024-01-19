def solution(word):
    global cnt
    global answer
    answer = 0
    
    arr = ['A', 'E', 'I', 'O', 'U']
    
    cnt = 0
    def back(n, sm, word):
        global cnt
        global answer
        cnt += 1

        if sm == word:
            answer = cnt-1
            return
        
        if n >= 5:
            return
        
        for i in arr:
            back(n+1, sm+i,  word)
            

    
    back(0, "", word)
        
        
    return answer
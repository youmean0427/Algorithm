def solution(files):
    files_sep = []
    answer = []
        
    for idx, f in enumerate(files):
        num_idx = []
        digit_check = 0
        
        for i in range(len(f)):
            if f[i].isdigit():
                digit_check = 1
                num_idx.append(i)
            elif digit_check == 1:
                break
                
        head = f[:num_idx[0]].upper()
        number = int(f[num_idx[0]:num_idx[-1]+1])
        tail = f[num_idx[-1]+1: ]
        
        files_sep.append((head, number, tail, idx))
        
    files_sep.sort(key=lambda x: (x[0], x[1]))

    for k in files_sep:
        answer.append(files[k[3]])
    return answer
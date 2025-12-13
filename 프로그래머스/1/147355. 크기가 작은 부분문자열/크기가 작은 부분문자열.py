def solution(t, p):
    k = len(p)
    cnt = 0
    
    for i in range(len(t) - k + 1):
        if t[i:i+k] <= p:   # 길이가 같으니 문자열 비교로 OK
            cnt += 1
            
    return cnt

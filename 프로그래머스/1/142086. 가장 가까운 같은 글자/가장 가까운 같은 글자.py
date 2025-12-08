def solution(s):
    last_index = {}   # 각 문자별 마지막 등장 위치 저장
    answer = []
    
    for i, ch in enumerate(s):
        if ch in last_index:
            # 이전에 나온 적이 있으면 거리 = 현재 위치 - 마지막 위치
            answer.append(i - last_index[ch])
        else:
            # 첫 등장이라면 -1
            answer.append(-1)
        
        # 현재 위치를 마지막 위치로 갱신
        last_index[ch] = i
    
    return answer

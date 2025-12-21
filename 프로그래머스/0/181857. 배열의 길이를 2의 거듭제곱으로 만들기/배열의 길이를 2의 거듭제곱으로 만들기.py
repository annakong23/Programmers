def solution(arr):
    n = len(arr)
    power = 1
    
    # n 이상인 가장 작은 2의 거듭제곱 찾기
    while power < n:
        power *= 2
    
    # 필요한 만큼 0 추가
    return arr + [0] * (power - n)

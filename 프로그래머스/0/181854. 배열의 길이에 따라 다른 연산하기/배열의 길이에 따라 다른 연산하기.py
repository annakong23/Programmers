def solution(arr, n):
    # 길이가 홀수면 짝수 인덱스, 짝수면 홀수 인덱스
    start = 0 if len(arr) % 2 == 1 else 1
    
    for i in range(start, len(arr), 2):
        arr[i] += n
    
    return arr

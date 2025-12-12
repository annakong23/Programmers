def solution(A, B):
    A.sort()              # 오름차순
    B.sort(reverse=True)  # 내림차순

    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer

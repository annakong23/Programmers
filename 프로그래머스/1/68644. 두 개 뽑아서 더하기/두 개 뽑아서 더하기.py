def solution(numbers):
    sums = set()

    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):  # 서로 다른 인덱스 + 중복 조합 방지
            sums.add(numbers[i] + numbers[j])

    return sorted(sums)

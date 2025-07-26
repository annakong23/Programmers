def solution(s):
    from collections import Counter
    count = Counter(s)
    result = sorted([char for char in count if count[char]==1])
    answer = ''.join(result)
    return answer
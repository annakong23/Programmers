def solution(sizes):
    sizes = [sorted(x) for x in sizes]
    max_values = [max(x) for x in zip(*sizes)]
    return max_values[0]*max_values[1]
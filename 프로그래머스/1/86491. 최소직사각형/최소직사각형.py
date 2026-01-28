# def solution(sizes):
#     lst = [sorted(x) for x in sizes]
#     return max(x[0] for x in lst) * max(x[1] for x in lst)















def solution(sizes):
    sizes = [sorted(x) for x in sizes]
    max_values = [max(x) for x in zip(*sizes)]
    return max_values[0]*max_values[1]
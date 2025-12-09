def solution(q, r, code):
    answer = []
    for i, ch in enumerate(code):
        if i % q == r:
            answer.append(ch)
    return "".join(answer)

def solution(sides):
    s_s = sorted(sides)
    if s_s[2]<s_s[0]+s_s[1]: answer=1
    else: answer=2
    return answer

def solution(sides):
    return 1 if max(sides) < sum(sides)-max(sides) else 2
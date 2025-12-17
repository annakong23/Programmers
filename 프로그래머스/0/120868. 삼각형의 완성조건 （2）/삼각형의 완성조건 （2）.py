def solution(sides):
    a, b = sorted(sides)
    
    # case 1: 기존 변이 가장 긴 변
    case1 = a  # (b - a + 1) ~ b → 개수는 a
    
    # case 2: x가 가장 긴 변
    case2 = a - 1  # (b + 1) ~ (a + b - 1)
    
    return case1 + case2

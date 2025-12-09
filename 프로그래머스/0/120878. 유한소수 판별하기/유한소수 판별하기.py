import math

def solution(a, b):
    # 1) 기약분수로 만들기
    g = math.gcd(a, b)
    b //= g
    
    # 2) 분모에서 2와 5만 제거
    for n in [2, 5]:
        while b % n == 0:
            b //= n
            
    # 3) 남은 값이 1이면 유한소수
    return 1 if b == 1 else 2

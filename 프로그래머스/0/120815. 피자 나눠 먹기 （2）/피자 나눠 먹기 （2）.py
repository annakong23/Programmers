import math

def solution(n):
    # 최소 필요한 피자 판 수 = n / gcd(6, n)
    return n // math.gcd(6, n)
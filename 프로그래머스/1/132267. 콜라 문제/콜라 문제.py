solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

# def solution(a, b, n):
#     answer = 0
#     empty = n  # 현재 가지고 있는 빈 병 수

#     while empty >= a:
#         # 이번에 교환 가능한 세트 수
#         exchange = empty // a
        
#         # 이번에 받는 콜라 수
#         get_cola = exchange * b
        
#         # 총 받은 콜라 수에 더하기
#         answer += get_cola
        
#         # 다음 턴에 가지고 있을 빈 병 수 갱신
#         empty = empty % a + get_cola
    
#     return answer

# def solution(my_string):
#     total = 0
#     temp = ''

#     for ch in my_string:
#         if ch.isdigit():
#             temp += ch
#         else:             
#             if temp != '':
#                 total += int(temp)
#                 temp = ''

#     # 마지막에 숫자로 끝나는 경우 처리
#     if temp != '':
#         total += int(temp)

#     return total

import re

def solution(my_string):
    return sum(map(int, re.findall(r'\d+', my_string)))

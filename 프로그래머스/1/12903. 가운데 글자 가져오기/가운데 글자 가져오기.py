# def solution(s):
#     if len(s)%2 != 0:
#         return s[len(s)//2]
#     else:
#         return s[(len(s)//2)-1: (len(s)//2)+1]
#     answer = ''
#     return answer

def solution(s):
    return (s[len(s)//2] if len(s)%2 != 0 else s[(len(s)//2)-1: (len(s)//2)+1])
    # return s[(len(s)-1)//2 : len(s)//2 + 1]

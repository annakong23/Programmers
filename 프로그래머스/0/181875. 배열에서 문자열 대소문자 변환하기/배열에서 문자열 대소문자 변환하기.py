# def solution(strArr):
#     answer = []
#     for i in range(0, len(strArr)):
#         if i%2==0: answer.append(strArr[i].lower())
#         else: answer.append(strArr[i].upper())
#     return answer


def solution(strArr):
    return [s.lower() if i%2==0 else s.upper() for i,s in enumerate(strArr)]
# def solution(str1, str2):
#     answer = []
#     for i,s in enumerate(str1):
#         answer.append(s)
#         answer.append(str2[i])
#     return ''.join(answer)

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i] 
    return answer
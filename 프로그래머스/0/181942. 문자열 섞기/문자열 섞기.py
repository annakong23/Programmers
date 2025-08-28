def solution(str1, str2):
    answer = []
    for i,s in enumerate(str1):
        answer.append(s)
        answer.append(str2[i])
    return ''.join(answer)
def solution(myString):
    answer = sorted(myString.split('x'))
    answer = list(filter(None, answer))
    print(answer)
    return answer
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        finish = commands[i][1]
        k = commands[i][2]
        answer.append(sorted(array[start-1: finish])[k-1])
    return answer

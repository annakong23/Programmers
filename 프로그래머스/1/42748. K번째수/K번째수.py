def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i,j,k=commands[a][0], commands[a][1], commands[a][2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
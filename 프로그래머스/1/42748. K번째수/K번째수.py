def solution(array, commands):
    num_list=[]
    for i in range(0,len(commands)):
        num_list.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return num_list














# def solution(array, commands):
#     answer = []
#     for a in range(len(commands)):
#         i,j,k=commands[a][0], commands[a][1], commands[a][2]
#         answer.append(sorted(array[i-1:j])[k-1])
#     return answer
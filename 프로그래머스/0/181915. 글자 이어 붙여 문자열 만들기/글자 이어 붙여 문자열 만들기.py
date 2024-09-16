def solution(my_string, index_list):
    answer = []
    for i in index_list:
        answer.append(my_string[i])
    answer = ''.join(answer)
    return answer

# def solution(my_string, index_list):
#     answer = ''.join([my_string[i] for i in index_list])
#     return answer


# def solution(my_string, index_list):
#     return ''.join([my_string[idx] for idx in index_list])
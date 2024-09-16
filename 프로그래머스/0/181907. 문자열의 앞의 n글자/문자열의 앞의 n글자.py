def solution(my_string, n):
    my_string = list(my_string)
    answer = my_string[:n]
    answer = ''.join(answer)
    return answer
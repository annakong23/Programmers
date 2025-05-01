#v1
def solution(num_list):
    return list(reversed(num_list))

#v2
def solution(num_list):
    return num_list[::-1]

#v3
def solution(num_list):
    num_list.reverse()
    return num_list
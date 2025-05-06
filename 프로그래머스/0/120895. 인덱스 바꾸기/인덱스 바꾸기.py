# def solution(my_string, num1, num2):
#     return ''.join(my_string[:num1]+my_string[num2]+my_string[num1+1:num2]+my_string[num1]+my_string[num2+1:])

def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)
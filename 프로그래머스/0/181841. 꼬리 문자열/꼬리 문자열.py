def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))











# def solution(str_list, ex):
#     answer = []
#     for word in str_list:
#         if ex not in word:
#             answer.append(word)
#     answer = ''.join(answer)
#     print(answer)
#     return answer

# def solution(str_list, ex):
#     return ''.join(filter(lambda x: ex not in x ,str_list))
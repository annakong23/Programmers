# def solution(arr):
#     answer = [arr[0]]
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[i-1]:
#             answer.append(arr[i])
#         else:
#             continue
#     return answer

def solution(arr):
    stack = []
    for x in arr:
        if not stack or stack[-1] != x:
            stack.append(x)
    return stack









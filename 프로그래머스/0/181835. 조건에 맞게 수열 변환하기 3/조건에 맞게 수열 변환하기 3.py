# def solution(arr, k):
#     if k%2==1:
#         return [i*k for i in arr]
#     else:
#         return [i+k for i in arr]

def solution(arr, k):
    return [i*k if k%2==1 else i+k for i in arr]
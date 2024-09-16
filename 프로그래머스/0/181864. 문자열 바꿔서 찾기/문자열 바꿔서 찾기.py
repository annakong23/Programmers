def solution(myString, pat):
    swapped =[]
    for char in myString:
        if char == 'A':
            swapped.append('B')
        elif char == 'B':
            swapped.append('A')
    swapped = ''.join(swapped)
    answer = 1 if pat in swapped else 0
    return answer

# def solution(myString, pat):
#     swapped = ''.join('B' if char =='A' else 'A' for char in myString)
#     answer = 1 if pat in swapped else 0
#     return answer
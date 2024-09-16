def solution(myString, pat):
    reverse =[]
    for char in myString:
        if char == 'A':
            reverse.append('B')
        elif char == 'B':
            reverse.append('A')
    reverse_str = ''.join(reverse)
    answer = 1 if pat in reverse_str else 0
    return answer
def solution(s, n):
    ans = []
    for ch in s:
        if ch == ' ':
            ans.append(' ')
        elif 'A' <= ch <= 'Z':
            # A~Z: 65~90
            ans.append(chr((ord(ch) - ord('A') + n) % 26 + ord('A')))
        else:  # 'a' <= ch <= 'z'
            # a~z: 97~122
            ans.append(chr((ord(ch) - ord('a') + n) % 26 + ord('a')))
    return ''.join(ans)

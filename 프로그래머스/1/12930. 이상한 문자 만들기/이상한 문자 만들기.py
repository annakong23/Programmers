def solution(s):
    answer = []
    
    for word in s.split(" "):    # 공백 그대로 유지 위해 split(" ")
        new_word = ""
        for i, ch in enumerate(word):
            if i % 2 == 0:
                new_word += ch.upper()
            else:
                new_word += ch.lower()
        answer.append(new_word)
    
    return " ".join(answer)

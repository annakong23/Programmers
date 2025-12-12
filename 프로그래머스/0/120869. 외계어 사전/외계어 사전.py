def solution(spell, dic):
    target = ''.join(sorted(spell))  # 기준 문자열 (spell 정렬)

    for word in dic:
        if len(word) != len(spell):  # 길이 다르면 애초에 불가능
            continue
        if ''.join(sorted(word)) == target:  # 알파벳 구성 완전히 동일한지 체크
            return 1

    return 2

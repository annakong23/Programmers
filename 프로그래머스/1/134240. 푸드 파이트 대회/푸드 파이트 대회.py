def solution(food):
    left = []

    # 1번 음식부터 마지막 음식까지
    for i in range(1, len(food)):
        cnt = food[i] // 2       # 한 사람당 먹을 수 있는 개수
        left.append(str(i) * cnt)

    left_str = "".join(left)
    answer = left_str + "0" + left_str[::-1]
    return answer

def solution(n, m, section):
    cnt = 0
    painted_end = 0  # 여기까지 칠해져 있음(구역 번호 기준)

    for s in section:
        if s > painted_end:          # 아직 안 칠한 구역이면
            cnt += 1
            painted_end = s + m - 1  # s부터 m칸 칠함

    return cnt

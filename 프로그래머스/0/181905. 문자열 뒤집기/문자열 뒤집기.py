def solution(my_string, s, e):
    # print(my_string[:s])
    # print(my_string[e:s-1:-1]) #마지막에 -1만 한다고 역순 출력이 아니라 슬라이싱할 인덱스도 거꾸로 써야 함
    # print(my_string[e+1:])
    answer = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return answer
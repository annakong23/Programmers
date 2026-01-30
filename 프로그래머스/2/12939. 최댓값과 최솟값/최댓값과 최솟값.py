def solution(s):
    nl=list(map(int, s.split()))
    return str(min(nl))+' '+str(max(nl))

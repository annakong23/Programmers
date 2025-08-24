def solution(s):
    pc,yc=0,0
    for i in list(s.lower()):
        if i=='p':
            pc += 1
        elif i=='y':
            yc += 1
    return pc==yc
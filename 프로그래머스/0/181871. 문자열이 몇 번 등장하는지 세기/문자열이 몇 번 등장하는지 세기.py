def solution(myString, pat):
    cnt=0
    for i in range(0,len(myString)-len(pat)+1):
        if pat in myString[i:i+len(pat)]:
            cnt+=1
    return cnt
N, M = map(int, input().split())

listen = set()
see = set()

for i in range(N):
    listen.add(input())
for j in range(M):
    see.add(input())
    
intersection = listen.intersection(see)
intersection = sorted(intersection)

print(len(intersection))
for name in intersection:
    print(name)
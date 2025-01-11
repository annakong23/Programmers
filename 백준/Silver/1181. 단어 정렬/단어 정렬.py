n = int(input())
a = set()
for _ in range(n):
    a.add(input())

a = list(a)    
a.sort()    
a.sort(key=len)

for i in a:
    print(i)
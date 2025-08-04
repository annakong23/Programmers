n = int(input())
files = []
for _ in range(n):
    files.append(input())

pattern = list(files[0])
for i in range(1,n):
    for j in range(len(pattern)):
        if pattern[j] != files[i][j]:
            pattern[j] = '?'
            
print(''.join(pattern))
n = int(input())
data = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age in data:
        data[age].append(name)
    else:
        data[age] = [name]

sorted_data = dict(sorted(data.items()))

for age, names in sorted_data.items():
    for name in names:
        print(age, name)
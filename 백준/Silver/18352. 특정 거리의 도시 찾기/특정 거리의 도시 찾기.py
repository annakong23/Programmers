from collections import deque


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# 최단 거리 초기화
distance = [-1] * (N + 1)
distance[X] = 0  # 시작점은 거리 0

# BFS로 최단 거리 계산
queue = deque([X])

while queue:
    current = queue.popleft()
    for next_city in graph[current]:
        if distance[next_city] == -1:  # 아직 방문하지 않은 도시
            distance[next_city] = distance[current] + 1
            queue.append(next_city)

# 결과 도출
result = [i for i in range(1, N + 1) if distance[i] == K]

# 출력
if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)
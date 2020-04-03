def bfs(r, c):
    global max_distance
    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[r][c] = 1
    q = [(r, c)]
    while q:
        rr, cc = q.pop(0)
        # 사방탐색
        for i in range(4):
            nr = rr + dx[i]
            nc = cc + dy[i]
            # 범위내에 있으면서 땅이고 방문한적 없는 경우
            if 0 <= nr < R and 0 <= nc < C and treasure_map[nr][nc] == 'L' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[rr][cc] + 1
                # 가장 긴 시간 갱신
                if visited[nr][nc] - 1 > max_distance:
                    max_distance = visited[nr][nc] - 1
                q.append((nr, nc))


R, C = map(int, input().split())
treasure_map = [[i for i in input()] for _ in range(R)]
searched = [[0 for _ in range(C)] for _ in range(R)]

# 사방탐색: 위, 오, 아, 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_distance = 0
for r in range(R):
    for c in range(C):
        # 땅 발견
        if treasure_map[r][c] == 'L' and searched[r][c] == 0:
            searched[r][c] = 1
            bfs(r, c)

print(max_distance)


def find(row, col):
    global layout
    stack = [[row, col]]
    layout[row][col] = 1
    space = 1
    while stack:
        cur = stack.pop()
        for i in range(4):
            nr = cur[0] + dx[i]
            nc = cur[1] + dy[i]
            if 0 <= nr < M and 0 <= nc < N and layout[nr][nc] == 0:
                stack.append([nr, nc])
                layout[nr][nc] = 1
                space += 1
    return space



M, N, K = map(int, input().split())
layout = [[0 for _ in range(N)] for _ in range(M)]

# 사각형들 배치
for _ in range(K):
    coordinates = [int(i) for i in input().split()]
    bottom_left = [M-coordinates[1]-1, coordinates[0]]
    top_right = [M-coordinates[3], coordinates[2]-1]
    for r in range(top_right[0], bottom_left[0]+1):
        for c in range(bottom_left[1], top_right[1]+1):
            layout[r][c] += 1

areas = 0
spaces = []
# 영역탐색
# 위, 오, 아, 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for r in range(M):
    for c in range(N):
        if layout[r][c] == 0:
            areas += 1
            spaces.append(find(r, c))

spaces.sort()
print(areas)
for space in spaces:
    print(space, end=' ')
print()



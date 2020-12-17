from collections import deque

N, M = [int(i) for i in input().split()]
map = [[int(i) for i in input().split()] for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]


def mark_land(r, c, mark):
    # 위, 오, 아, 왼
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append([r, c])

    while q:
        cur_r, cur_c = q.popleft()
        visited[cur_r][cur_c] = True
        map[cur_r][cur_c] = mark
        for i in range(4):
            next_r = cur_r + dx[i]
            next_c = cur_c + dy[i]

            # 해당 섬에 속하는 땅 발견
            if 0 <= next_r < N and 0 <= next_c < M and map[next_r][next_c] and not visited[next_r][next_c]:
                q.append([next_r, next_c])


def find_land(mark):
    global island_cnt

    for r in range(N):
        for c in range(M):
            if not visited[r][c]:
                # 섬 발견
                if map[r][c]:
                    island_cnt += 1
                    mark_land(r, c, mark)
                    find_land(mark+1)
                # 바다인 경우
                else:
                    visited[r][c] = True


def find_bridge(r, c):
    # 아래 탐색
    bridge_len = 0
    cur_r = r + 1
    while True:
        if cur_r >= N:
            bridge_len = 0
            break
        elif not map[cur_r][c]:
            bridge_len += 1
            cur_r += 1
        else:
            if map[r][c] != map[cur_r][c]:
                break
            else:
                bridge_len = 0
                break

    if bridge_len > 1:
        island1 = map[r][c]
        island2 = map[cur_r][c]
        if adj[island1][island2]:
            if adj[island1][island2] > bridge_len:
                adj[island1][island2] = bridge_len
                adj[island2][island1] = bridge_len
        else:
            adj[island1][island2] = bridge_len
            adj[island2][island1] = bridge_len

    # 오른쪽 탐색
    bridge_len = 0
    cur_c = c + 1
    while True:
        if cur_c >= M:
            bridge_len = 0
            break
        elif not map[r][cur_c]:
            bridge_len += 1
            cur_c += 1
        else:
            if map[r][c] != map[r][cur_c]:
                break
            else:
                bridge_len = 0
                break

    if bridge_len > 1:
        island1 = map[r][c]
        island2 = map[r][cur_c]
        if adj[island1][island2]:
            if adj[island1][island2] > bridge_len:
                adj[island1][island2] = bridge_len
                adj[island2][island1] = bridge_len
        else:
            adj[island1][island2] = bridge_len
            adj[island2][island1] = bridge_len


# 지도에서 섬을 찾고 섬마다 번호 부여
island_cnt = 0
find_land(1)

adj = [[0 for _ in range(island_cnt+1)] for _ in range(island_cnt+1)]

# 섬 사이를 잇는 다리를 찾아 인접행렬에 거리를 기록
for r in range(N):
    for c in range(M):
        if map[r][c]:
            find_bridge(r, c)

# 최소 신장 트리
INF = float('inf')
p = [0] * (island_cnt+1)
key = [INF] * (island_cnt+1)
mst = [False] * (island_cnt+1)

# 1번 섬부터 시작
key[1] = 0

cnt = 0
total_distance = 0
while cnt < island_cnt:
    # key 값이 최소이고 mst에 안 속한 섬 찾기
    min_key = INF
    u = -1
    for i in range(1, island_cnt+1):
        if key[i] <= min_key and not mst[i]:
            min_key = key[i]
            u = i
    mst[u] = True
    total_distance += min_key
    for w in range(1, island_cnt+1):
        if adj[u][w] and not mst[w] and adj[u][w] < key[w]:
            key[w] = adj[u][w]
            p[w] = u

    cnt += 1

if total_distance != INF:
    print(total_distance)
else:
    print(-1)


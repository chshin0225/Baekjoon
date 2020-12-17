
N, M = map(int, input().split())

board = [[i for i in input()] for _ in range(N)]

for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            bx, by = r, c
            continue
        elif board[r][c] == 'R':
            rx, ry = r, c
            continue


T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    cabbages = [[int(i) for i in input().split()] for _ in range(K)]
    cabbages = [[cabbage[1], cabbage[0]] for cabbage in cabbages]
    patch = [[0 for a in range(M)] for b in range(N)]

    for cabbage in cabbages:
        x, y = cabbage
        patch[x][y] = 1

    worms = 0
    visited = []
    stack = []
    while cabbages:
        cabbage = cabbages.pop()
        if cabbage not in visited:
            stack.append(cabbage)
            visited.append(cabbage)
            worms += 1
        while stack:
            x, y = stack.pop()
            # 위, 오, 아, 왼
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and patch[x+dx[i]][y+dy[i]] == 1 and [x+dx[i], y+dy[i]] not in visited:
                    visited.append([x+dx[i], y+dy[i]])
                    stack.append([x+dx[i], y+dy[i]])


    print(worms)

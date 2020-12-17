import copy

N, M, D = [int(i) for i in input().split()]
board = [[int(i) for i in input().split()] for _ in range(N)] + [[2] * M]


# 궁수 3명 위치 선정
def pick_position(columns, archers, index, start):
    global sel, picked, kill_cnt, max_cnt

    # 궁수 위치 선정 후 게임 시작
    def play(arr):
        global kill_cnt

        # 적이 한명이라도 남아있는지 체크
        def enemy_exists():
            for row in range(N):
                for col in range(M):
                    if playing_board[row][col]:
                        return True
            return False

        # 궁수와 적 사이의 거리 측정
        def distance(N, r, a, c):
            return abs(N-r) + abs(a-c)

        playing_board = copy.deepcopy(board)

        # 적들이 전부 사라질 때까지 게임 진행
        while enemy_exists():
            # 이번 턴에서 궁수들이 죽일 적들
            enemy_to_kill = []

            # 각 궁수마다 죽일 적 탐색
            for a in arr:
                target = []
                min_distance = D + 1

                for r in range(N-1, N-D-1, -1):
                    for c in range(a-D, a+D+1):
                        if 0 <= r < N and 0 <= c < M and abs(N-r) + abs(a-c) <= D:
                            if playing_board[r][c]:
                                if distance(N, r, a, c) < min_distance:
                                    min_distance = distance(N, r, a, c)
                                    target = [r, c]
                                elif distance(N, r, a, c) == min_distance:
                                    if c < target[1]:
                                        target = [r, c]

                # 탐색해낸 적이 죽일 적들 리스트에 안 들어있으면 넣기
                if target and target not in enemy_to_kill:
                    enemy_to_kill.append(target)

            if enemy_to_kill:
                # 적들 죽이기
                for enemy in enemy_to_kill:
                    r, c = enemy
                    playing_board[r][c] = 0
                    kill_cnt += 1

            # 적들 한 칸씩 전진
            for r in range(N-1, -1, -1):
                for c in range(M):
                    if playing_board[r][c]:
                        if 0 <= r+1 < N:
                            playing_board[r+1][c] = 1
                        playing_board[r][c] = 0

    if index == 3:
        # 궁수들 위치 선정 끝나면 게임 진행
        play(sel)
        # 최대 죽일 수 있는 적의 수 갱신
        if kill_cnt > max_cnt:
            max_cnt = kill_cnt
        kill_cnt = 0
        return
    for idx in range(start, columns):
        if not picked[idx]:
            picked[idx] = True
            sel[index] = idx
            pick_position(columns, archers, index+1, idx)
            picked[idx] = False

sel = [0] * 3
picked = [False] * M
kill_cnt = 0
max_cnt = 0

pick_position(M, 3, 0, 0)

print(max_cnt)
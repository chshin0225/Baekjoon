
N, M, x, y, K = map(int, input().split())

layout = [[int(i) for i in input().split()] for _ in range(N)]

# for row in layout:
#     print(row)

directions = [int(i) for i in input().split()]

dice = [[-1, 0, -1], [0, 0, 0], [-1, 0, -1], [-1, 0, -1]]

for direction in directions:
    # 동
    if direction == 1:
        if y + 1 >= M:
            continue

        y += 1

        left = dice[1][0]
        top = dice[1][1]
        right = dice[1][2]
        bottom = dice[3][1]
        dice[1][0] = bottom
        dice[1][1] = left
        dice[1][2] = top
        dice[3][1] = right
        # print(dice)

    # 서
    elif direction == 2:
        if y - 1 < 0:
            continue

        y -= 1

        left = dice[1][0]
        top = dice[1][1]
        right = dice[1][2]
        bottom = dice[3][1]
        dice[1][0] = top
        dice[1][1] = right
        dice[1][2] = bottom
        dice[3][1] = left
        # print(dice)

    # 북
    elif direction == 3:
        if x - 1 < 0:
            continue

        x -= 1

        top = dice.pop(0)
        dice.append(top)
        dice[1][0] = dice[0][0]
        dice[1][2] = dice[0][2]
        dice[0][0] = dice[0][2] = -1
        # print(dice)
    # 남
    else:
        if x + 1 >= N:
            continue

        x += 1

        bottom = dice.pop()
        dice.insert(0, bottom)
        dice[1][0] = dice[2][0]
        dice[1][2] = dice[2][2]
        dice[2][0] = dice[2][2] = -1
        # print(dice)

    cur_value = layout[x][y]
    new_bottom = dice[3][1]
    if cur_value == 0:
        layout[x][y] = new_bottom
    else:
        dice[3][1] = cur_value
        layout[x][y] = 0

    new_top = dice[1][1]
    print(new_top)
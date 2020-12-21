import copy
from collections import deque

N, M, K = [int(i) for i in input().split()]
matrix = [[0 for _ in range(M+1)]] + [[0] + [int(i) for i in input().split()] for _ in range(N)]
orders = [[int(i) for i in input().split()] for _ in range(K)]

# 회전 연산 수행 순서 정하기
sel = [-1] * K
visited = [False] * K

# 연산에 맞게 회전
def turn(arr, order):
    r, c, s = order
    n = 0
    while n < s + 1:
        start_r = r - s + n
        start_c = c - s + n
        end_r = r + s - n
        end_c = c + s - n

        nums = deque()
        cur_r = start_r
        cur_c = start_c

        if start_r == end_r and start_c == end_c:
            nums.append(arr[cur_r][cur_c])
        else:
            while cur_c < end_c:
                # print(arr[cur_r][cur_c])
                nums.append(arr[cur_r][cur_c])
                cur_c += 1

            while cur_r < end_r:
                # print(arr[cur_r][cur_c])
                nums.append(arr[cur_r][cur_c])
                cur_r += 1

            while cur_c > start_c:
                # print(arr[cur_r][cur_c])
                nums.append(arr[cur_r][cur_c])
                cur_c -= 1

            while cur_r > start_r:
                # print(arr[cur_r][cur_c])
                nums.append(arr[cur_r][cur_c])
                cur_r -= 1
            nums.rotate(1)

        cur_r = start_r
        cur_c = start_c
        rotated_idx = 0
        if start_r == end_r and start_c == end_c:
            pass
        else:
            while cur_c < end_c:
                # print(arr[cur_r][cur_c])
                arr[cur_r][cur_c] = nums[rotated_idx]
                rotated_idx += 1
                cur_c += 1

            while cur_r < end_r:
                # print(arr[cur_r][cur_c])
                arr[cur_r][cur_c] = nums[rotated_idx]
                rotated_idx += 1
                cur_r += 1

            while cur_c > start_c:
                # print(arr[cur_r][cur_c])
                arr[cur_r][cur_c] = nums[rotated_idx]
                rotated_idx += 1
                cur_c -= 1

            while cur_r > start_r:
                # print(arr[cur_r][cur_c])
                arr[cur_r][cur_c] = nums[rotated_idx]
                rotated_idx += 1
                cur_r -= 1

        n += 1


# 주어진 연산 순서에 맞게 수행
def execute(ordered_orders):
    global min_sum
    arr = copy.deepcopy(matrix)
    for order in ordered_orders:
        turn(arr, order)
    for row in arr[1:]:
        row_sum = sum(row)
        if row_sum < min_sum:
            min_sum = row_sum

def perm(i, k):
    if i == k:
        execute(sel)
    else:
        for idx in range(K):
            if not visited[idx]:
                visited[idx] = True
                sel[i] = orders[idx]
                perm(i+1, K)
                visited[idx] = False

min_sum = N * M * 100
perm(0, K)

print(min_sum)
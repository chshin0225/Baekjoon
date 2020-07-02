
def check_fit(x, y, paper_size):
    possible = True
    for i in range(x, x+paper_size):
        for j in range(y, y+paper_size):
            if not board[i][j]:
                possible = False
                break
    if possible:
        return True
    return False


def completed(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                return False
    return True


def dfs(x, y):
    global answer
    if board[x][y]:
        for paper_size in range(5, 0, -1):
            if paper_pieces[paper_size] and x + paper_size <= 10 and y + paper_size <= 10:
                if check_fit(x, y, paper_size):
                    paper_pieces[paper_size] -= 1
                    for i in range(x, x + paper_size):
                        for j in range(y, y + paper_size):
                            board[i][j] = 0
                    if y < 9:
                        dfs(x, y + 1)
                    elif x < 9:
                        dfs(x + 1, 0)
                    else:
                        total = 0
                        for i in range(1, 6):
                            total += 5 - paper_pieces[i]
                        if total < answer:
                            answer = total
                        return
                    paper_pieces[paper_size] += 1
                    for i in range(x, x + paper_size):
                        for j in range(y, y + paper_size):
                            board[i][j] = 1
    if y < 9:
        dfs(x, y+1)
    elif x < 9:
        dfs(x+1, 0)
    else:
        total = 0
        for i in range(1, 6):
            total += 5 - paper_pieces[i]
        if total < answer:
            answer = total
        return


N = 10

board = [[int(i) for i in input().split()] for _ in range(N)]
paper_pieces = {i: 5 for i in range(1, 6)}
answer = float('inf')

dfs(0, 0)

if answer == float('inf'):
    answer = -1

print(answer)






























# import copy
#
# def check_fit(paper_size):
#     global placement
#     for r_start in range(N-paper_size+1):
#         for c_start in range(N-paper_size+1):
#             if board[r_start][c_start]:
#                 possible = True
#                 for i in range(r_start, r_start+paper_size):
#                     for j in range(c_start, c_start+paper_size):
#                         if not board[i][j]:
#                             possible = False
#                             break
#                 if possible:
#                     placement = [r_start, c_start]
#                     return True
#     return False
#
#
# def completed(arr):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]:
#                 return False
#     return True
#
#
# def not_possible(arr):
#     for a in arr:
#         if a != -1:
#             return False
#     return True
#
# N = 10
#
# init_board = [[int(i) for i in input().split()] for _ in range(N)]
#
# # 모든 경우의 수를 넣기 위한 리스트
# possibilities = []
#
# # 만약 처음부터 아무 종이도 붙일 필요가 없다면
# if completed(init_board):
#     possibilities.append(0)
# else:
#     # 사용할 수 있는 가장 큰 사이즈의 종이 제한을 점점 줄여나가면서 탐색하기
#     for biggest_size in range(5, 0, -1):
#         board = copy.deepcopy(init_board)
#         paper_pieces = {i: 5 for i in range(1, 6)}
#         cnt = 0
#         while not completed(board):
#             possibility_flag = True
#             for paper_size in range(biggest_size, 0, -1):
#                 placement = []
#                 # 해당 사이즈의 종이를 붙일 수 있다면
#                 if check_fit(paper_size):
#                     # 해당 종이가 남아있다면
#                     if paper_pieces[paper_size]:
#                         # 종이를 붙일 곳의 가장 왼쪽 상단 좌표
#                         r, c = placement
#                         # 종이 붙인 곳의 값을 0으로 바꾸기
#                         for i in range(r, r+paper_size):
#                             for j in range(c, c+paper_size):
#                                 board[i][j] = 0
#                         # 종이 하나 사용했으니 cnt + 1
#                         cnt += 1
#                         # 종이 하나 사용했으니 남은 종이 - 1
#                         paper_pieces[paper_size] -= 1
#                         # 다음으로 붙일 수 있는 종이 탐색을 다시 5 사이즈부터 시작하기 위해 break
#                         break
#                     else:
#                         # 만약 사용하고 싶은 크기의 종이가 남아있지 않다면 이 옵션은 가능하지 않은 경우라서 그냥 break
#                         possibility_flag = False
#                         break
#             # 만약 가능하기 않은 옵션이라면 cnt는 -1이 됨
#             if not possibility_flag:
#                 cnt = -1
#                 break
#
#         # 모든 경우의 수를 리스트에 넣기
#         possibilities.append(cnt)
#
# if possibilities == [0]:
#     answer = 0
# elif not_possible(possibilities):
#     answer = -1
# else:
#     answer = 25
#     for p in possibilities:
#         if 0 < p < answer:
#             answer = p
#
# print(answer)



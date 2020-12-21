from collections import deque

N = int(input())
equation = [int(i) if i.isnumeric() else i for i in input()]
equation = [equation[i//2] if i % 2 else '_' for i in range(N*2)] + ['_']

def calculate(equation):
    global max_result
    s = deque()
    for cur in equation:
        if cur == '_':
            continue
        elif cur == ')':
            sub_s = deque()
            while True:
                i = s.pop()
                if i != '(':
                    sub_s.append(i)
                else:
                    break
            sub_result = sub_s.pop()
            while sub_s:
                i = sub_s.pop()
                if isinstance(i, str):
                    num = sub_s.pop()
                    if i == '*':
                        sub_result *= num
                    elif i == '-':
                        sub_result -= num
                    else:
                        sub_result += num
            s.append(sub_result)
        elif cur == '(':
            s.append(cur)
        else:
            s.append(cur)

    result = s.popleft()
    while s:
        i = s.popleft()
        if isinstance(i, str):
            num = s.popleft()
            if i == '*':
                result *= num
            elif i == '-':
                result -= num
            else:
                result += num

    if result > max_result:
        max_result = result




def close(equation, idx):
    i = idx + 1
    for i in range(idx+1, N*2+1):
        if equation[i] == '_' and isinstance(equation[i-1], int) and 2 < i - idx < 7:
            equation[i] = ')'
            calculate(equation)
            if N*2 - i > 5:
                open(equation, i+1)
            equation[i] = '_'

def open(equation, idx):
    for idx in range(idx, N*2+1):
        if equation[idx] == '_' and idx + 1 < N * 2 + 1 and isinstance(equation[idx+1], int) and N * 2 - idx > 2:
            equation[idx] = '('
            close(equation, idx)
            equation[idx] = '_'

max_result = -2**31
calculate(equation)
open(equation, 0)
print(max_result)


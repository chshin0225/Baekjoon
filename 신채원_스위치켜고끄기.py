# 스위치 개수
N = int(input())
# 스위치들
lights = [int(i) for i in input().split()]
# 학생 수
s = int(input())
# 학생들의 성별과 받은 수
students = [list(map(int, input().split())) for _ in range(s)]

def switch(i):
    if i == 1:
        return 0
    else:
        return 1

def palindrome(a):
    if a == a[len(a) - 1:: -1]:
        return True
    return False

for student in students:
    sex, number = student
    # 남학생일 때
    if sex == 1:
        lights = [switch(lights[i]) if (i+1) % number == 0 else lights[i] for i in range(len(lights))]
    # 여학생일 때
    else:
        center_idx = number - 1
        diff = 0
        while palindrome(lights[center_idx - diff:center_idx + diff + 1]):
            if palindrome(lights[center_idx - diff - 1:center_idx + diff + 2]) and center_idx - diff - 1 >= 0 and center_idx + diff + 1 < N:
                diff += 1
            else:
                break
        switches_to_change = lights[center_idx - diff:center_idx + diff + 1]
        lights = [switch(lights[i]) if i in range(center_idx-diff, center_idx+diff+1) else lights[i] for i in range(len(lights))]
for light_idx in range(len(lights)):
    print(lights[light_idx], end=' ')
    if (light_idx + 1) % 20 == 0:
        print()

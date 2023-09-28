n = int(input())
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def backtracking(x):
    global ans
    if x == n:
        ans += 1
        return

    for i in range(0, n):
        row[x] = i
        if is_promising(x):
            backtracking(x+1)


backtracking(0)
print(ans)
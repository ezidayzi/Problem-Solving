t = int(input())

for i in range(t):
    n1 = int(input())
    l1 = list(map(int, input().split()))
    l1.sort()

    n2 = int(input())
    l2 = list(map(int, input().split()))

    ans = [0] * n2

    for j in range(n2):
        start = 0
        end = n1 - 1
        while start <= end:
            mid = (start + end) // 2

            if l1[mid] == l2[j]:
                ans[j] = 1
                break
            elif l1[mid] < l2[j]:
                start = mid + 1
            else:
                end = mid - 1

    for a in ans:
        print(a)

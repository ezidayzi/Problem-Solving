n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
answer = [0] * m

card.sort()

start = 0
end = n-1

for i in range(len(check)):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start+end)//2

        if check[i] == card[mid]:
            answer[i] = 1
            break

        elif check[i] < card[mid]:
            end = mid - 1

        else:
            start = mid + 1


print(' '.join(map(str,answer)))
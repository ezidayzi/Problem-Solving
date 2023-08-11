N, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

start = 0
end = 0

check = [0] * (max(nums) + 1)
answer = 0

while start < N and end < N:
    if check[nums[end]] < K:
        check[nums[end]] += 1
        end += 1
    else:
        check[nums[start]] -= 1
        start += 1
    answer = max(answer, end - start)
print(answer)
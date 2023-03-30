# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 수

def solution(nums):
    # 소수 판별 함수(2이상의 자연수에 대하여)
    def is_prime_number(x):
        # 2부터 (x - 1)까지의 모든 수를 확인하며
        for i in range(2, x):
            # x가 해당 수로 나누어떨어진다면
            if x % i == 0:
                return False  # 소수가 아님
        return True  # 소수   임

    answer = -1
    array = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if is_prime_number(sum):
                    array.append(sum)
    answer = len(array)
    return answer

print(solution([1,2,7,6,4]))
from itertools import permutations

def solution(numbers):
    def is_prime_number(x):
        if x == 0 or x == 1:
            return False

        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    answer = 0
    nums = [n for n in numbers]  # numbers를 하나씩 자른 것
    per = []
    for i in range(1, len(numbers) + 1):  # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))  # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per]  # 각 순열조합을 하나의 int형 숫자로 변환

    new_nums = list(set(new_nums))
    for num in new_nums:
        if is_prime_number(num):
            print(num)
            answer += 1

    return answer
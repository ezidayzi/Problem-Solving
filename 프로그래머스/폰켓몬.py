# N마리의 폰켓몬 중 N/2마리 가져가도 좋음
# 폰켓몬 종류에 따라 번호를 붙여 구분
# 같은 종류의 폰켓몬 = 같은 번호
# N/2마리의 폰켓몬을 선택하는 방법 중 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아
# 그때의 폰켓몬 종류 번호의 개수

def solution(nums):
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        print(unique_types)
        return len(nums) / 2
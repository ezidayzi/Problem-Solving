# 숫자로 이루어진 문자열 t와 p
# t에서 p와 길이가 같은 부분 문자열 중
# 부분 문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나우는 횟수

def solution(t, p):
    answer = 0
    array = []

    for x in range(0, len(t)-len(p)+1):
        array.append(t[x: x+len(p)])

    for temp in array:
        if int(p) >= int(temp):
            answer = answer+1
    return answer

print(solution("500220839878", "7"))
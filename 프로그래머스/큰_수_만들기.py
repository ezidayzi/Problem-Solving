# k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자?

def solution(number, k):
    answer = ''
    stack = []

    for n in number:
        if len(stack) == 0:
            stack.append(n)
        else:
            while n > stack[-1] and k > 0:
                stack.pop()
                k -= 1
                if len(stack) == 0:
                    break
            stack.append(n)
    answer = ''.join(stack) if k == 0 else ''.join(stack[:-k])
    return answer
# 어떤 과학자가 발표한 논문 n 편 중, h 번 이상 인용된 논문이 h편 이상이고
# 나머지 논문은 h번 이하 인용
# h의 최댓값은? (h-index)

def solution(citations):
    answer = 0
    citations.sort()  # 정렬
    for i in range(0, len(citations)):
        if(citations[i] >= len(citations) - i):  # i번째 citation 이상의 논문 개수와 지금 논문의 인용 수 비교
            answer = max(answer, len(citations) - i)  # answer에 저장(max값)
    return answer
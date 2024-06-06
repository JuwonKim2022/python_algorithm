# <2. 합격생>
# 코테 합격생 수를 구하려고 한다.
# 매개변수 score에 시험 친 수햄생들의 시험 점수가 주어지고, 매개변수 k에 합격 커드라인 점수가 주어지면 자격증 시험에 합격한 수를 구해 반환하는 프로그램을 작성하시오.
def sol_0002(score, k):
    answer = 0
    n = len(score)

    for i in range(n):
        if score[i] >= k:
            answer = answer + 1

    return answer

print(sol_0002([60,50,80,90,55,70,65,45], 60))
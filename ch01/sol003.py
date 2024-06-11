# <3. 연속된 1의 길이>
# 매개변수 nums에 0과 1로 된 수열이 주어지면, 1이 연속된 부분수열 중 가장 긴 부분수열의 길이 반환하는 프로그램을 작성하시오.

def sol_0003(nums):
    answer = 0
    cnt = 0

    for x in nums:
        if x == 1:
            cnt += 1
        else:
            answer = max(answer, cnt)
            cnt = 0

    answer = max(answer, cnt)

    return answer

print(sol_0003([0,1,0,1,1,1,1,1,0,1,1,1,1,1]))
# < 6-5. 카드점수>
# N개의 카드가 일렬로, 각 카드에 숫자 적힘
# 카드 양쪽 끝 중 하나 고를 수 있음, k개 가져갈 수 있음
# 각 카드 숫자가 매개변수 nums에, 가져갈 카드 개수가 k
# 얻을 수 있는 최대 점수는

print('=====[6-5]=====')
def sol_0605(nums, k):
    answer = 0
    n = len(nums)

    print(nums)

    for i in range(k+1):
        sumN = 0
        for j in range(i):
            sumN += nums[j]
        for j in range(n-k+i, n):
            sumN += nums[j]
        answer = max(answer, sumN)

    return answer

print(sol_0605([2,3,7,1,2,1,5],4))

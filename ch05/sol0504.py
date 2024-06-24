# < 4-4. 두 수의 차>
# 매개변수 nums 수열, 원소 중 두 수의 차가 가장 작은 쌍을 찾아 반환
# 원소 수열은 유일값으로 구성, 값이 여러 개면 모두 다 출력
# 두 수는 오름차순
print('=====[4-4]=====')
def sol_0404(nums):
    n = len(nums)
    minN = 10000000
    answer = []

    for i in range(n):
        for j in range(i+1, n):
            diff = abs(nums[i] - nums[j])
            if diff < minN:
                minN = diff

    for i in range(n):
        for j in range(i+1, n):
            diff = abs(nums[i] - nums[j])
            if diff == minN:
                answer.append(sorted([nums[i], nums[j]]))

    return answer

print(sol_0404([3,8,1,5,12]))
print(sol_0404([2,1,3,5,4]))
print(sol_0404([5,10,15,20,25,11]))
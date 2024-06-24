# < 5-5. 두 수의 차>
# 매개변수 nums 수열, 원소 중 두 수의 차가 가장 작은 쌍을 찾아 반환
# 원소 수열은 유일값으로 구성, 값이 여러 개면 모두 다 출력
# 두 수는 오름차순
print('=====[5-5]=====')
def sol_0505(nums):
    n = len(nums)
    minN = 10000000000
    answer = []
    nums.sort()

    for i in range(1,n):
        diff = nums[i] - nums[i-1] #압하고만 비교해도 됨
        minN = min(minN, diff)

    for i in range(1,n):
        diff = nums[i] - nums[i-1]
        if diff == minN:
            answer.append([nums[i-1], nums[i]])

    return answer

print(sol_0505([3,8,1,5,12]))
print(sol_0505([2,1,3,5,4]))
print(sol_0505([5,10,15,20,25,11]))
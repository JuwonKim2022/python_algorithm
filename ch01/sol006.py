from collections import deque
# <6. 두 수의 합>
# 정수 수열 안에서 수열의 원소 두 개의 합이 target값이 되는 경우 찾는 중
# 매개변수 nums에 길이가 n인 수열, 매개변수 target에 자연수 값
# 이 수열 안에서 두 개의 원소의 합이 정수 target앖이 되는 두 원소를 구해 배열에 오름차순으로 담아 반환 (오직 한가지 경우만 주어짐, 한 원소 두번 더하기 안됨)
# nums의 각 원소는 유일값, 닶이 없을 경우 [0.0]
def sol_006(nums, target):
    zero = [0] * 2
    answer = deque(zero)
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                answer.pop()
                answer.pop()
                answer.append(nums[i])
                answer.append(nums[j])
                return list(sorted(answer))
    return list(answer)

print(sol_006([7,9,2,13,3,15,8,11], 12))



def sol_0061(nums, target):
    answer = [0] * 2
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return sorted([nums[i], nums[j]])
    return list(answer)
print(sol_0061([7,9,2,13,3,15,8,11], 12))
print(sol_006([1,1,1,1,1], 12))
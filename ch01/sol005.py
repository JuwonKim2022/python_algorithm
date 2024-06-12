from collections import deque
# <5. 중복제거>
# 오름차순으로 정렬된 수열이 주어지면 중복된 값을 제거
# 유일값으로 구성된 내림차순 수열 만들기
# 매개변수 nums에 길이가 n인 수열, 중복값 제거하고 유일값만 구성된 내림차순 수열을 배열에 담아 반환
def sol_0005(nums):
    answer = deque()
    answer.appendleft(nums[0])
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            answer.appendleft(nums[i])
    return list(answer)

print(sol_0005([0,1,1,1,2,2,2,3]))
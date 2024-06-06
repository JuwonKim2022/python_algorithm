# <1. 최솟값의 위치>
# 수열의 원소에서 가장 작은 값을 찾고 싶다.
# 매개변수 nums에 길이가 n인 수열이 주어지면 수열의 원소 중에서 가장 작은 값을 찾아 그 값의 nums 배열의 인덱스 번호를 반환하는 프로그램을 작성하시오.
# 배열의 인덱스 번호는 0부터 시작
# 3 <= nums <= 100,000 : 10만 이상이면 O(n^2)은 안됨
def sol_0001(nums):
    answer = 0
    miniNum = 10000000
    n = len(nums)

    for i in range(n):
        if nums[i] < miniNum:
            miniNum = nums[i]
            answer = i

    return answer

print(sol_0001([7,10,5,3,2,15,19]))
#<7-6. 고정된 숫자 >
# 오름차순 정렬 일차원 배열
# 인덱스 번호와 자기 자신값이 같으면 이 원소는 고정된 숫자
# nums = 오름차순으로 정렬된 정부 배열
# 고정된 숫자 반환하는 프로그램, 값은 유일값
# 없을 경우 -1

from bisect import bisect_left, bisect_right

print('=====[7-6]=====')
def sol_0706(nums):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == mid:
            return nums[mid]
        if nums[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(sol_0706([-3,-2,0,1,3,5,8,9,12]))
print(sol_0706([1,2,3,4,5,6,7,8,9]))
print(sol_0706([0,2,3,4,5,6,7,8,9,10,11,12]))
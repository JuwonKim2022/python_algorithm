#<7-1. 이진탐색 - O(lofN)>
# nums 오름차순으로 정렬된 정수 배열, target에 찾고자 하는 값
# nums배열에서 target의 인덱스 번호 찾아 반환하는 프로그램
# 값이 없으면 -1
print('=====[7-1]=====')
def sol_0701(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            left = mid+1
        else:
            right = mid-1

    return -1

print(sol_0701([2,5,7,8,10,15,20,24,25,30],8))
print(sol_0701([-5,-2,-1,3,8,9,12,17,23],2))


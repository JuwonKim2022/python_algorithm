#<7-5. 트럭 찾기 >
#이삿집센터 여러 트럭, 각 트럭 총 무게제한 있음
#이사비용 = 선택한 트럭 무게 * 10
#nums = 각 트럭 무게 제한 오름차순, wight = 이사하는 짐 총 무게
#짐 실을 수 있는 최소 비용 찾아 트럭 인덱스 수 구하기
#트럭 없을 경우 -1

from bisect import bisect_left, bisect_right

print('=====[7-5]=====')
def sol_0705(nums, weight):
    #원소 중 무게보다 크거나 같은 것 중에서, 가장 작은 것 인덱스 번호
    answer = bisect_left(nums, weight)
    return -1 if answer == len(nums) else answer

    # left = 0
    # right = len(nums)
    # while left < right:
    #     mid = (left + right)//2
    #     if weight > nums[mid]:
    #         left = mid + 1
    #     else:
    #         right = mid
    # return -1 if right==len(nums) else right

print(sol_0705([100,120,150,160,165,170,175,180,190,200], 170))
print(sol_0705([20,30,40,50,60,70], 90))
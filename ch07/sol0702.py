#<7-2. Lower bound Seasrch>
#찾고자 하는 값보다 크거나 같은 것 중, 가장 작은 값 찾아주는 이분검색법
print('=====[7-2]=====')
def sol_0702(nums, weight):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left+right)//2
        if weight > nums[mid]:
            left = mid+1
        else:
            right = mid-1

    return -1 if right == len(nums) else right

print(sol_0702([100,120,150,160,165,170,175,180,190,200],180))
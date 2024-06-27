#<6-6, 카드점수 고도화>
#슬라이딩 윈도우 사용 -> 범위 지정하고 한칸 씩 이동하며 비교
print('=====[6-6]=====')
def sol_0606(nums, k):
    total = sum(nums)
    m = len(nums)-k #남는 갯수
    score = 0

    for i in range(m):
        score += nums[i]

    minS = score

    #슬라이딩 윈도우
    left = 0
    for right in range(m,len(nums)):
        score += (nums[right]-nums[left])
        left += 1

        minS = min(minS, score)

    return total - minS

print(sol_0606([2,3,7,1,2,1,5],4))
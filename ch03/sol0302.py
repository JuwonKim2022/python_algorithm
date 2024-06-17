from collections import *

# <3-2. 빈도수>
# 해시맵으로 풀기
print('=====[3-2]=====')
def sol_0302(nums):
    answer = -1
    #1번
    # nHash = defaultdict(int)
    # for x in nums:
    #     nHash[x] += 1
    # print(nHash)
    #2번
    nHash = Counter(nums)

    for hkey in nHash:
        if nHash[hkey] == 1:
            answer = max(answer, hkey)

    return answer

print(sol_0302([3,9,2,12,9,12,8,7,9,12]))
from collections import *
# < 3-3. 자기 분열수
# 자기 분열수 = 배열의 원소 중 자기 자신의 숫자만큼 빈도수를 갖는 숫자
# 매개변수 = nums 에 자연수가 원소인 배열이 주어지면 이 배열에서 자기 분열수 중 가장 작은 수를 찾아 반환하는 프로그램
# 존재하지 않으면 -1
print('=====[3-3]=====')
def sol_0303(nums):
    answer = 100000000
    nHash = Counter(nums)
    print(nHash)

    for hkey in nHash:
        if nHash[hkey] == hkey:
            answer = min(answer, hkey)

    return -1 if answer == 100000000 else answer

print(sol_0303([1,2,3,1,3,3,2,4]))
from collections import *

# < 3-6. 두 수의 합
# 정수 수열 안에서 수열의 원소 두 개의 합이 target값 되는 경우 찾기
# 매개변수 = nums에 길이 n인 수열, 매개변수 target 자연수
# 두 원소를 구해 배열에 오름차순으로 담아 반환
#조건 : 답 한 가지인 경우만 주어짐, 한 원소 두 번 더하기 안됨, 답 없으면 [0,0]
print('=====[3-6]=====')
def sol_0306(nums, target):

    answer = [0]*2
    nH = defaultdict(int)

    for x in nums:
        y = target - x
        if y in nH:
            return sorted([x,y])
        nH[x] = 1
        print('nH = ', nH[x])
    print('==end===')
    return answer

print(sol_0306([7,3,2,13,9,15,8,11], 12))
print(sol_0306([7,5,12,20], 15))
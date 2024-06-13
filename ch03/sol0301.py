# < 3-1. 빈도수1>
# 매개변수 nums에 길이가 n인 수열이 주어짐
# 수열의 원소 중에서 빈도수가 1인 가장 큰 숫자 반환하는 프로그램 작성
# 숫자 없을 경우 -1 반환

#키 = 실제 수 , 밸류 = 빈도수
#다이렉트 어드레스 테이블
print('=====[3-1]=====')
def sol_0301(nums):
    answer = -1
    cnt = [0]*1001
    for x in nums:
        cnt[x] += 1
    for i in range(1000, 0, -1):
        if cnt[i] == 1:
            return i

    return answer

print(sol_0301([3,9,2,12,9,12,8,7,9,12]))
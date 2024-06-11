from collections import deque

# <4. 수열의 회전 >
# 정수 수열 회전하고 싶다.
# 매게변수 nums에 길이가 n인 수열이 주어지고,
# 매개변수 k에 뒤로 이동시키고 싶은 원소의 개수 주어짐
# 수열에서 k번 뒤로 이동된 수열 반환

def sol_0004(nums, k):
    #deque로 변경
    answer = deque(nums)
    for i in range(k):
        answer.append(answer.popleft())
    return list(answer)

print(sol_0004([3,7,1,5,9,2,8], 3))
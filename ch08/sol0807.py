from collections import deque
print('=====[8-7]=====')
# < 8-7. 고장난 프린터 >
# 프린트 순서 : 먼저 2개 작업 프린트, 3번째 작업은 순서상 맨 뒤로 보냄
# 매개변수 nums에 프린트 요청 작업 순서,
# 가장 마지막 프린트 하는 번호는?

def sol_0807(nums):
    queue = deque(nums)
    answer = 0

    while queue:
        for _ in range(2):
            if len(queue)>=2:
                queue.popleft()
        queue.append(queue.popleft())
        if len(queue)==1:
            return queue[0]

print(sol_0807([3,1,4,5,2,6,7]))
print(sol_0807([10,8,3,1,4,5,2,11,13,6,7,12,9,14]))
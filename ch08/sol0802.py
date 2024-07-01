print('=====[8-2]=====')
# < 8-2. 큐 >
# 한 쪽 끝에서 자료를 넣고 반대쪽에서 삭제되는 FIFO 형식 자료 구조
# 먼저 추가한 것을 먼저 꺼냄

# 파이썬에서는 쿠 사용
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
print(len(queue)==0)
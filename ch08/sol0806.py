print('=====[8-6]=====')
# < 8-6. 샌드위치 >
# 식빵 + 토마토 + 식빵 형태의 샌드위치 제작
# 식빵 = 1, 토마토 = 2
# 배열에서 중간 중간에 조건 만족하는 배열에서 샌드위치 만드려 함
# 최종 만들어지는 샌드위치 갯수는?

def sol_0806(nums):
    stack = []
    answer = 0
    for x in nums:
        if x==1 and len(stack)>=2 and stack[-1]==2 and stack[-2]==1:
            answer += 1
            stack.pop()
            stack.pop()
        else:
            stack.append(x)

    return answer

print(sol_0806([1,1,1,2,1,1,2,1,2,1]))
print(sol_0806([1,1,1,1,1,1,1]))
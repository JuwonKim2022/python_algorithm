print('=====[8-3]=====')
# < 8-3. 올바른 괄호 >
# 괄호 문자열 입력, 올바른 괄호면 YES, 아니면 NO

from collections import deque
stack = []
answer = "YES"
def sol_0803(s):
    for x in s:
        if x == ')':
            if len(stack)==0:
                return "NO"
            else:
                stack.pop()
        else:
            stack.append(x)
    if len(stack) > 0:
        return "NO"
    return answer

print(sol_0803("((()))()"))
print(sol_0803("())()"))
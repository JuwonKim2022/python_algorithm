print('=====[8-5]=====')
# < 8-5. 연속된 문자 지우기 >
# 매개변수 s에 문자열. 이웃한 두 개의 문자가 같으면 두 문자 제거
# 최종 반환되는 문자열 출력

def sol_0805(s):
    stack = []
    for x in s:
        if stack and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)

    return "".join(stack)

print(sol_0805("acbbcaa"))
print(sol_0805("bacccaba"))
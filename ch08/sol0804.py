print('=====[8-4]=====')
# < 8-4. 백스페이스 >
# 문자열 순서대로 자판을 쳐서 s문자열 작성함. 중간에 #은 백스페이스 의미
# 최종 반환되는 문자열 출력

def sol_0804(s):
    stack = []
    for x in s:
        if x == '#':
            if len(stack) > 0: #빈 스캑이면 거짓, 하나라도 있으면 참
                stack.pop()
        else:
            stack.append(x)

    return "".join(stack)

print(sol_0804("abc##ec#ab"))
print(sol_0804("kefd#ef##s##"))

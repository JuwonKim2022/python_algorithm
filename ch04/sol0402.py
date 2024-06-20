# <4-3. 청소 로봇>
# [0,0]에서 시작
# U=위로 한칸, R=우측 한칸, L=좌측 한칸, D=아래 한칸
# 매개변수 moves 문자열 순서로 명령
# 명령 수행 후 최종 위치 반환하는 프로그램, 격자판 벗어나는 명령 없음
print('=====[4-3]=====')
def sol_0403(moves):
    answer = [0]*2
    # print(answer)

    for x in moves:
        # print(x)
        if x == 'U':
            answer[0] = answer[0] - 1
        elif x == 'D':
            answer[0] = answer[0] + 1
        elif x == 'R':
            answer[1] = answer[1] + 1
        else:
            answer[1] = answer[1] - 1

    return answer

print(sol_0403('RRRDDDLU'))
print(sol_0403('DDDRRRDDLL'))

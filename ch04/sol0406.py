# <4-6. 로봇이동>
# [0,0]에서 시작, 3시 방향 보는 중
# G = 보고 있는 방향으올 한칸, R=우측 90도 회전, L=좌측 90도 회전
# 매개변수 moves 문자열 순서로 명령
# 명령 수행 후 최종 위치 반환하는 프로그램, 격자판 벗어나는 명령 없음
print('=====[4-6]=====')
def sol_0406(moves):
    x = y = 0
#         12,3,6,9
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    d = 1 #로봇이 보는 방향(인덱스번호)

    for c in moves:
        if c == 'G':
            x = x + dx[d]
            y = y + dy[d]
        elif c == 'R':
            d = (d+1)%4
        elif c == 'L':
            d = (d+3)%4 #파이썬은 d = (d-1)%4 도 가능
        else:
            continue

    return [x,y]

print(sol_0406('GGGRGGG'))
print(sol_0406('GGGGGGGRGGGRGGRGGGLGGG'))
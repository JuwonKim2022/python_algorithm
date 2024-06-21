# <4-5. 청소 로봇 - 벽에 가는 문자도 들어감>
# [0,0]에서 시작
# U=위로 한칸, R=우측 한칸, L=좌측 한칸, D=아래 한칸
# 매개변수 n 격자판 크기, 매개변수 moves 문자열 순서로 명령
# 명령 수행 후 최종 위치 반환하는 프로그램, 격자판 벗어나는 명령 있음
print('=====[4-5]=====')
def sol_0405(n, moves):
    x = y = 0
#         12,3,6,9
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    direct = ['U', 'R', 'D', 'L']

    for c in moves:
        for k in range(4):
            if c == direct[k]:
                nx = x + dx[k]
                ny = y + dy[k]

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
    

        x = nx
        y = ny

    return [x,y]

print(sol_0405(5, 'RRRDDDUUUUUUL'))
print(sol_0405(7, 'DDDRRRDDLL'))
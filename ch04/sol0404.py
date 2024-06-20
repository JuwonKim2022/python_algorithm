# <4-4. 로봇 리팩토링>
print('=====[4-4]=====')
def sol_0404(moves):
    x = y = 0
#         12,3,6,9
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    direct = ['U', 'R', 'D', 'L']

    for c in moves:
        for k in range(4):
            if c == direct[k]:
                x = x + dx[k]
                y = y + dy[k]

    return [x,y]

print(sol_0404('RRRDDDLU'))
print(sol_0404('DDDRRRDDLL'))
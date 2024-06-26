# <5-7. 위험지역>
# n*n 이차원 배열에 특정 지역에 지뢰정보 주어짐
# 1은 지뢰, 0은 안전지대
# 지뢰 주변 상하좌우대각선의 빈 땅을 위험지역이라 함
# 매개변수 board, 지도, 위험지역이 총 몇 개인가 반환하는 프로그램
print('=====[5-7]=====')
def sol_0507(board):
    answer = 0
#         12, 1, 3,4,5,6,7,9,11
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and board[nx][ny] == 0:
                        answer += 1
                        board[nx][ny] = 2

    print(board)
    return answer

print(sol_0507([[0,0,0,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]])) #14
# print(sol_0407([[0,1,0,0,0,1,0],[0,1,1,0,0,0,0],[0,0,0,1,0,0,1],[0,0,0,0,0,1,0],[1,0,0,0,0,0,0],[1,0,0,1,0,0,1],[1,0,0,1,0,0,0]]))
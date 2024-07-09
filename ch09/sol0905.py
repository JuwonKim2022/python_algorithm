print('=====[9-5]=====')
# < 9-5. 검정색 영역구하기 >
# 5*5 화면, 검정색1, 흰색0
# 상하좌우로 검전색 연결되어있으면 한 영역으로 간주
# 매개변수 board 모니터 화면의 격자정보, 검정 영역 총 몇 개인가 구하기

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS2(x,y,board):
    board[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx>=0 and nx<5 and ny>=0 and ny<5 and board[nx][ny]==1:
            DFS2(nx,ny,board)

def sol_0905(board):
    answer = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                answer += 1
                DFS2(i,j,board)
    return answer

print(sol_0905([[0,1,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,1,1,0]]))

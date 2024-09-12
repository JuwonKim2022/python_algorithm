# < 10-5. 검정색 영역 픽셀수 구하기 >
# 5*5 화면, 검정색1, 흰색0
# 상하좌우로 검전색 연결되어있으면 한 영역으로 간주
# 매개변수 board 모니터 화면의 격자정보, 검정 영역의 픽셀 수를 순서대로 배열에 담아 반환
# 영역의 순서는 각 영역의 행번호, 열번호 순으로

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

def DFS3(x,y,board):
    global cnt
    board[x][y] = 0
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx>=0 and nx<5 and ny>=0 and ny<5 and board[nx][ny]==1:
            DFS3(nx,ny,board)

def sol_1006(board):
    global cnt
    answer = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                cnt = 0
                DFS3(i,j,board)
                answer.append(cnt)
    return answer

print(sol_1006([[0,1,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,1,1,0]]))
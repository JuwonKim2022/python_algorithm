# <4-1. 웅덩이>
# 매개변수 nums에 n행 n열의 이차원 배열에 격자판 정보 주어짐
# 각 격자에 높이 쓰여짐, 상하좌우 인접한 지역 숫자가 모두 자신보다 클 경우 이 지역을 웅덩이
# 격자 가장자리는 1000으로 초기화
# 주어진 격자에 웅덩이 몇 개인가 갯수 반환하는 프로그램 작성
print('=====[4-2]=====')
def sol_0402(nums):
    answer = 0
#         12,3,6,9
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    n = len(nums)

    for i in range(n):
        for j in range(n):
            flag = True #웅덩이라고 가정하고
            for k in range(4): #4방향 확인
                nx = i + dx[k]
                ny = j + dy[k]
                if nx>=0 and nx<n and ny >= 0 and ny<n and nums[i][j] >= nums[nx][ny]:
                    flag = False
                    break #하나라도 발견되면 더 조사할 필요 없어서 브래이크
            if flag == True:
                answer += 1

    return answer

print(sol_0402([[10,20,50,30,20],[20,30,50,70,90],[10,15,25,80,35],[25,35,40,55,80],[30,20,35,40,90]]))
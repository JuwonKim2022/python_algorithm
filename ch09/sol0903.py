print('=====[9-3]=====')
# < 9-3. 이진트리 깊이우선 탐색 >
# 조건1 : 부모 -> 사긱
# 조건2 : 왼쪽 자식노드 : 2n -> 오른쪽 사직노드 : 2n+1

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)

DFS(1)
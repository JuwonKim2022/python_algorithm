print('=====[9-1]=====')
# < 9-1. 재귀함수 >
# 자기 자신을 호출하는 함수, 스택 환경에서 작동

def DFS(n):
    if n == 0:
        return
    else:
        print(n, end=' ')
        DFS(n-1)

DFS(5)
print()

def DFS(n):
    if n == 0:
        return
    else:
        DFS(n-1)
        print(n, end=' ')

DFS(5)
print()
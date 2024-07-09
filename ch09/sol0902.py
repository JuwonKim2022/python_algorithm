print('=====[9-2]=====')
# < 9-2. n! 구하기 >
# 매개변수 n에 자연수 입력되면 n팩토리얼 값 구하기

def sol_0802(n):
    if n == 1:
        return 1
    else:
        return n * sol_0802(n-1)

print(sol_0802(5))
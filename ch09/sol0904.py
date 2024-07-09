print('=====[9-4]=====')
# < 9-4. 피보나치 수열 >
# n번째 항은 n-`항과 n-2항을 합하여 구함
# 매개변수 n 주어지면, 피보나치 수열의 n번째 항 구하기

def sol_0904(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sol_0904(n-1) + sol_0904(n-2)

print(sol_0904(5))
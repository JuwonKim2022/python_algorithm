from collections import *

# < 3-5. 팰린드롭 길잉
# 문자열 중어지면 만들 수 있는 최대길이 펠린드롬 만들어 길이 구하기
# 매개변수 = s 문자열, 모두 소문자
print('=====[3-5]=====')
def sol_0305(s):
    sH = Counter(s)
    odd = 0
    print(sH)

    for key in sH:
        if sH[key] % 2 == 1:
            odd += 1

    return len(s) - odd + 1 if odd > 0 else len(s)

print(sol_0305("abcbbbccaaeee"))
print(sol_0305("afgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(sol_0305("aabbccddee"))
from collections import *
# < 3-4. 팰린드롭 확인
# 소문자로만 주어진 문자열 주어지면 해당 문자열의 문자들의 순서를 재배치하여 팰린드롬(회문) 만들 수 있는지 확인
# 매개변수 = s 문자열이 주어지면 해당 문자열이 재배치 통해 팰린드롬 만들 수 있으면 True, 없으면 False
print('=====[3-4]=====')
def sol_0304(s):
    odd = 0
    nHash = Counter(s)
    print(nHash)

    for hkey in nHash:
        if nHash[hkey] % 2 == 1:
            odd = odd + 1

    return True if odd <= 1 else False

print(sol_0304("abacbaa"))
print(sol_0304("abaaceeffkckbaa"))
print(sol_0304("abcabbcc"))
print(sol_0304("abcabc"))
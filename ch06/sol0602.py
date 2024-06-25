# < 6-2. 버스>
# 버스 무게 제한
# 매개변수 weight에 각 학생 몸무게, limit 버스 수용 능력
# 버스에 탈 수 있는 최대 인원수
print('=====[6-2]=====')
def sol_0602(weight, limit):
    answer = 0
    sumW = 0
    weight.sort()
    
    for x in weight:
        if sumW + x > limit:
            break
        sumW += x
        answer += 1

    return answer

print(sol_0602([300,100,230,120,90,150,60], 700))
print(sol_0602([50,90,70,120,300,200,150,180,190], 1000))
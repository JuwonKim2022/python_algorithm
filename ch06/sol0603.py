# < 6-3. 최대 사과 개수>
# 여러 종류의 사과 박스, 각 박스마다 들어가는 사과 갯수 다름
# 트럭에 박스 싣기, 최대 갯수 제한
# 매개변수 box에 각 박스 종류의 정보, limit에 트럭 박스 최대 개수
# 트럭에 실을 수 있는 사과 최대 갯수 반환 프로그램

print('=====[6-3]=====')
def sol_0603(box, limit):
    answer = 0
    box.sort(key = lambda v : -v[1])
    print(box)

    for x in box:
        cnt = min(limit, x[0])
        answer += (cnt * x[1])
        limit -= cnt
        if limit == 0:
            break

    return answer

print(sol_0603([[2,20],[2,10],[3,15],[2,30]], 5))
print(sol_0603([[3,40],[5,20],[5,70],[1,80],[5,30],[3,35]], 15))

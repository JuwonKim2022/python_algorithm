print('=====[8-1]=====')
# < 8-1. 스택 >
# 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO 형식 자료 구조

# 파이썬에서는 리스트를 스택처럼 사용

arr = [1,2,3]
print(arr)
arr.append('item1')
print(arr)
arr.append('item2')
print(arr)
arr.pop()
print(arr)
#스택 가장 위에 것 반환
print(arr[-1])
#스택 비어 있을 때 True 반환
print(len(arr)==0)
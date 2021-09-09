array = [i for i in range(20) if i % 2 ==1]
print(array)
array = [i * i for i in range(1, 10)]
print(array)

# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2==1]
print(array)
# 일반적인 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3, 5} # 집합 자료형
# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)
key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)
item_list = data.items()
print(item_list)
data = set([1,1,2,3,4,5])
print(data)

# 입력을 위한 전형적인 소스코드 1)
n = input()
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)
# 빠르게 문자열 입력 받기
import sys
from typing import Collection, Counter
data = sys.stdin.readline().rstrip()
print(data)

# 출력을 위한 전형적인 소스코드
a = 1
b = 2
print(a, b)
print(7, end = " ")
print(8, end = " ")

answer = 7
print('정답은' + str(answer) + '입니다.')

# f-string 예제
answer = 7
print(f"정답은 {answer}입니다.")

# 조건문 예제
x = 15
if x >= 10:
    print("x >= 10")
if x >= 0:
    print("x >= 0")
if x >= 30:
    print("x > = 30")

# 조건문 간소화
score = 85
if score >= 80: result = "Success"
else: result = "Fail"

score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

# 반복문
i = 0
result = 0
while i <= 9:
    result+= i
    i+= 1
print(result)

array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

scores = [90, 85, 77, 65, 97]
for i in range(5):
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")

# 함수
def add(a, b):
    return a+b
print(add(3,7))

def add(a,b):
    print('함수의 결과:', a +b)
add(3,7)

a = 10
def func():
    global a
    a += 1
    print(a)
func()

#람다 표현식
print((lambda a,b: a+b)(3,7))
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
def my_key(x):
    return x[1]
print(sorted(array, key = my_key))
print(sorted(array, key = lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a+b, list1, list2)
print(list(result))

# 유용한 표준 라이브러리
result = eval("(3+5)*7")
print(result)

result = sorted([9, 1, 4, 3, 8])
reverse_result = sorted([9, 1, 4, 3, 8], reverse=True)
print(reverse_result)

array = [('홍길동', 35), ('이순신', 75), ('아무개',50)]
result = sorted(array, key = lambda x: x[1], reverse=True)
print(result

# 순열과 조합
# from itertools import permutations
# data = ['A', 'B', 'C']
# result = list(permutations(data, 3))
# print(result)

# from collections import Counter
# counter = Counter(['red', 'blue', 'red', 'green','blue'])
# print(counter['blue'])
# print(counter['green'])
# print(dict(counter))
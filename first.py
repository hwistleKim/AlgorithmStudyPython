a = 7777777777777777777777777777777777
print(a)

# round 함수
# //몫 연산자 %나머지 연산자 **거듭제곱 연산자 /나누기 연산자
# 리스트 자료형 인덱싱과 슬라이싱 컴프리헨션

# array = [i for i in range(10)]
## print(array)

# array [i for i in range(20) if i % 2 == 1]

# for문 반복을 위한 변수 값 무시할때 언더바 사용 가능

# .append() 원소 하나 삽입
# .sort() (reverse = true) 오름차순, 내림차순
# reverse() 원소 순서 뒤집기
# insert(삽입할 위치 인덱스, 삽입 할 값)
# count(특정 값) 개수 세기
# remove(특정 값) 특정 값 원소 제거, 값을 가진 원소 여러개면 하나만 제거

# 집합 자료형

result = [i for i in a if i not in remove_set]
print(result)

# 문자열 자료형 " \" " escape 문자형 문자열 변경은 불가능

# 튜플 자료형

# 사전 자료형 해쉬 테이블 

# 집합 자료형 중복 제거 합집합 교집합 차집합 | & -
# update, remove


# 입출력

# input() 한 줄의 문자열 입력
# map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# ex> 공백을 기준으로 구분된 데이터를 입력 받을때
# data list(map(int, input().split()))
# a, b, c = map(int, input().split())

# 빠르게 입력받기 sys.stdin.readline().rstrip()
# print(data) ,를 이용하여 띄어쓰기 로 구분하여 출력 end=" " 로 변경 가능 default 엔터
# f string
# answer = 7
# print(f"정답은 {answer}입니다")

# 조건문 elif and or not
# in 연산자 pass 키워드


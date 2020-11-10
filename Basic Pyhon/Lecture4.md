# 함수
## 구조
  - 파이썬 함수는 함수명(매개변수): 
  - 수행할 문장 1 ...
  - return 리턴값   의 형태로 구성되어 있음
~~~ python
 def sum(a,b) :
     result = a+ b
     return result
~~~
  - 위의 값을 실행해도 정의한 것이기 때문에 값이 나오지는 않는다. 
  - 입력값과 출력값이 없을 수도 있고, 결과값이 없을 수도 있다. 
  - 여러 개의 인자를 변수로 받고 싶을 때는, *agrs 사용하면 여러 인자를 한번에 받을 수 있음
~~~python
def sum_many(*args) :
    sum = 0
    for i in args :
        sum = sum + i
    return sum
print(sum_many(1,2,3,4))
~~~
  - 언제나 함수의 리턴값은 하나이다. 여러개의 리턴값이 나온다면, 튜플의 형태로 하나의 값이 나오게 된다

## 초기값과 변수
  - 기본값을 설정하는 값은 제일 뒤로 가야함 (인자들의 입력 순서 때문)
~~~python
def say_my_name(name,old,man = True):
    print("My name is %s" %name)
    print("I am %d years old" %old)
    if man :
        print(" I am man")
    else : 
        print("I am not man")
say_my_name('kk', 23)
~~~
  - 함수 내에서 정의한 변수는 지역 변수! 함수 내에서만 사용되고 함수 밖에 있는 변수에 영향을 주지 않는다.
  - 필요한 경우 함수의 return 값으로 돌려주고, 밖에 있는 변수에 함수의 Return 값을 할당시켜 주면 바꿀 수 있다.  
  - 다른 방법으로 global을 사용하여 전역변수로 사용할 수 있으나,,
## 람다식
  - 파이썬에서는 간편하게 람다식을 사용할 수 있음 
~~~python
#def add(a,b):
#    return a+ b
add = lambda a, b : a+ b
~~~
  - def를 못쓰는 상황에서 활용할 때에 간편하다. 아래처럼 손 쉽게 list를 작성할 수 있다. 
~~~python
myList = [lambda a, b : a+b, lambda a, b : a*b]
~~~
## 입력과 출력
  - input 함수로 사용자의 입력값을 Return값으로 받을 수 있음
  - print 함수 심화 : +를 통해 String Data를 이어서 보여줄 수 있음
  - print 함수는 기본적으로 한줄씩 출력을 함 / end 옵션을 통해 붙여서 사용도 가능

## 파일 읽기/쓰기
~~~python
f = open("C:/Python/새파일.txt" , 'w', encoding = "UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
~~~
## 한줄 읽기
~~~python
f = open("새파일.txt", 'r', encoding= 'UTF-8')
line = f.readline()
print(line)
f.close()
~~~
## 여러줄 읽기-1
~~~python
f = open("새파일.txt", 'r', encoding= 'UTF-8')
while True :
    line = f.readline()
    if not line : break
    print(line)
f.close()
~~~
## 여러줄 읽기-2
~~~python
f = open("새파일.txt", 'r', encoding= 'UTF-8')
lines = f.readlines()
for line in lines()
    print(line, end="")
f.close()
~~~
## 통째로 읽기
~~~python
f = open("새파일.txt", 'r', encoding= 'UTF-8')
data = f.read()
print(data)
f.close()
~~~
  - open("새파일.txt", "w" )는 새롭게 쓰게 됨
  - open("새파일.txt", "a" )는 추가로 쓰게 됨

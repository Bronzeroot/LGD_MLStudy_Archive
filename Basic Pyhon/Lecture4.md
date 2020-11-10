#함수
1. 구조
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

 1. 초기값
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
  - 

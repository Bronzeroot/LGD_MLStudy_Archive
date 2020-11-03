# 제어문 

 1. If문(조건문) 
  - 조건에 따라 다른 결과 값을 출력해줌 
  - Indent에 주의해서 사용해야 오류가 나오지 않음 
  - Bool 자료형으로 실행할 Code를 다르게 설정할 수 있음 
  -  |는 or로 사용함 &는 and와 같음
  - x or y 는 둘중 하나만 True면 True, and 는 모두 True여야 True
  - if 1 in [1,2,3] : True 값 반환 / if 1 not in [1,2,3] : False 반환
  - pass를 사용하여 해당 값에 아무 일도 일어나지 않을 수 있음. 
  - elif를 통해 다른 조건 추가 가능
  - *조건부 표현식* : message = "success" if score >= 60 else "failure" 로 간단하게 표현 가능
  
 1. Whlie문 & for문(반복문)
  - 반복적으로 계속 수행해야하는 작업 처리
  - 역시 Indent에 주의해야 오류가 나오지 않음
  - break : while문안에 들어가서 특정한 조건에서 while문을 중단 시킬 수 있음
  - continue : while문안에 들어가서 특정한 조건에서 아래 코드를 실행하지 않고 다시 위로 돌아가게 함   
  - for문의 구조 ::  for 변수 in 리스트(튜플, 문자열) :   >> 뒤의 집합에서 순서대로 하나씩 출력하여 값을 돌려줌
  - for문에서도 continue 똑같이 사용 가능 (조건을 만족하는 경우 아래 내용 실행 없이 위로 올라가서 다시 For문을 진행시킴) 
  - Break역시 동일
  - *이중 for 문 : 안쪽 for문이 모두 실행된 후에, 밖에 for문에 카운트가 하나 올라감* 
  - 리스트 내포 (List Comprehension)  result = [num*3 for num in a]
'''
  result = [num *3 for num in a]
    result = []
        for num in a :
        if num&2 ==0:
            result.append(num*3)
'''
   

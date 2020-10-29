 # 파이썬 강좌_자료형 by 조코딩
 # 변수는 Data를 담는 상자다.  
   =를 기준으로 왼쪽에 오른쪽에 있는 데이터를 넣는다는 약속
  1. 숫자형
     - 정수형 1,2, -2 -> int
     - 실수형 1.23, 2.64 -> float
     - 지수형 4.24e10  4.24*1000000000
     - 8진수 
     - 16진수
        
  1. 문자열 
     - "" , '' , """ , '''
     - 문자열 자료는 str(string)으로 사용함
     - \'를 사용하면 \뒤에' 이것을 문자로 인식하게 됨, \\도 \를 문자로 쓸 수 있게 해줌
     - \n을 사용하면 한줄 띄울 수 있음 (이스케이프 코드)
     - """ ㅇㄹㄴㄹ """ 이렇게 3개로 감싸는 경우 이스케이프 코드를 사용하지 않고 편하게 사용 가능 
     - 문자열도 더하고 곱할 수 있음
     - **인덱싱** - []로 사용가능. a='Python' a[0] = 'P' / a[1] = 'y'/ a[-1] = 'n'
     - **슬라이싱** - a[ 이상: 미만: 간격]  ex:) a='20010331Rainy'  a[::2] = 처음부터 끝까지 2칸씩 간다
     - 문자열 포메팅 %s  / .format() 을 사용해서 포매팅도 가능함
     - count, find, .count() / .find()함수 사용 , find에서 결과값 없을 시 -1을 출력함
     - join 문자열 삽입 
     - .replace( "a", "b") a를 b로 바꿈
     - split() 띄어쓰기 기준으로 잘라서 리스트를 만들어줌
     
  1. 리스트
     - d = ["a","b","C","d"] 하나의 변수에 여러개의 변수를 넣어서 관리할 수 있음
     - 리스트 안에 리스트도 넣어서 관리 가능
     - 리스트의 인덱싱, 슬라이싱도 가능
     - 리스트 교체 삭제 수정 가능
     - append는 제일 뒤에 추가, insert는 몇번째에 넣을지 지정 가능
     - pop, count, extend 등의 함수도 사용 가능 (extend는 리스트에 리스트를 붙일 수 있음
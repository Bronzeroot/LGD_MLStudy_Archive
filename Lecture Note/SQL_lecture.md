# File은 한계가 있음

1. DB는 File의 한계를 보완하기 위해서 만들어진 것
 - 소중한 Data를 안전하고 편리하게 사용하기 위해서 만들어짐
 - DB는 일어날 수 있는 일들이 많기 때문에 기능 또한 굉장히 많음
 - CRUD 입력(생성,수정,삭제) 출력(Read)만 할 줄 알더라도 DB를 안다고 할 수 있음
 - 나머지는 부가적인 기능
 - 스키마는 관련 Data Table을 저장하는 Directory와 비슷한 개념
 - 여러 스키마가 모여있는 것이 DB Server이다

1. Oracle (생성하기 / 시작하기)
 - User를 생성하면 사용자 별 Schema를 사용하게 됨
 - cmd - sqlplus - sys as SYSDBA - CREATE USER '''' IDENTIFIED BY '''';
 - GRANT DBA TO '''' ;
 - 

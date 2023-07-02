# Django를 이용해서 todolist 만들기

[원본레포](https://github.com/kimbareum/Todolist) 에서 API를 구현해서 SPA 형식으로 페이지를 구성해보려고 했으나, 성능면에서 서버사이드 렌더링을 기반으로 페이지를 전환하는것보다 느린것 처럼 느껴져서 서버사이드 렌더링으로 페이지를 재구성한 레포입니다.  
원본레포는 추후 수정할 예정입니다.

## 목표

1. 로그인기능 구현해서 개인적인 todolist 관리.
2. 카테고리를 분류해서 카테고리에 따른 todo를 관리.
3. todo완료시 취소선으로 완료를 표기할 수 있도록 하기.
4. 카테고리와 각각의 todo에 대한 CRUD 기능 구현.

## 개발환경 및 개발 기간

-   개발환경  
    Django, HTML, CSS, JavaScript, sqlite

-   개발기간  
    2023년 6월 16일 ~ 2023년 6월 20일 + 2023년 6월 23일 ~ 

## 사용예제

<img src="./readme/%EB%A9%94%EC%9D%B8%ED%8E%98%EC%9D%B4%EC%A7%80.png">

    - 메인페이지. 로그인 회원가입 및 간단한 페이지 소개.  

<img src="./readme/%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%8E%98%EC%9D%B4%EC%A7%80.png" width='49%'>
<img src="./readme/%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%8B%A4%ED%8C%A8.png"width='49%'>  

    - 로그인 페이지 및 로그인 실패 시 메세지 표기 예시.

<img src="./readme/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%ED%8E%98%EC%9D%B4%EC%A7%80.png" width='49%'>
<img src="./readme/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EC%8B%A4%ED%8C%A8.png" width='49%'>

    - 회원가입 페이지 및 회원가입 실패 시 메세지 표기 예시.

<img src="./readme/%EB%A6%AC%EC%8A%A4%ED%8A%B8%ED%8E%98%EC%9D%B4%EC%A7%80.png">

    - 할일 리스트 페이지.
    - 할일의 카테고리를 추가 할 수 있고, 카테고리 별로 구분된 할일을 관리할 수 있음.
    - 추가된 카테고리 명을 선택하면 선택할 곳에 해당 카테고리 명에 밑줄처리가 되고, 해당 카테고리 페이지로 이동.
    - 카테고리 옆의 펜 표시와 X 표시를 통해 수정과 삭제가 가능.
    - 할일추가는 할일 표시부 하단의 큰 검정바탕의 + 버튼을 통해서 가능.
    - 할일의 수정 및 삭제 또한 할일이 표시된 박스의 펜버튼과 X 버튼을 통해서 가능.
    - 할일이 표시된 박스의 좌상단의 체크박스를 누르면 취소선 표시가 가능.

<img src="./readme/%ED%95%A0%EC%9D%BC%20%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%88%98%EC%A0%95%20%EC%B0%BD.png" width='49%'>
<img src="./readme/%ED%95%A0%EC%9D%BC%20%EC%B6%94%EA%B0%80%20%EB%B0%8F%20%EC%88%98%EC%A0%95%20%EC%B0%BD.png" width='49%'>

    - 할일의 카테고리 입력 및 수정 창
    - 할일 각각의 입력 및 수정 창

## 개발과정

- 데이터 베이스 구조  
    <figure>
        <img src="./readme/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4.png">
        <figcaption>해당 이미지는 erdcloud 에서 작성했습니다.</figcaption>
    </figure>

    - 회원마다 여러개의 카테고리를 가질 수 있고, 카테고리 별로 여러개의 할 일을 가질 수 있는 데이터베이스 구조로 설계했습니다.  
    - 회원 테이블에는 Django의 기본값인 username과 password를 이용하였고, 리스트페이지에서 상단에 표기할 별명을 nickname 행으로 추가했습니다.  
    - 카테고리 테이블에는 카테고리의 명인 name과 외래키인 user_id로 구성하고, 할 일 테이블에는 할 일의 제목인 title, 할 일의 상세 내용인 content, 할 일의 완료여부인 is_clear, 그리고 외래키인 category_id로 구성했습니다.  
    - 데이터베이스의 생성과 조작은 Django ORM을 이용하여, user모델은 django.contrib.auth.models의 AbstractUser를 상속받아서 생성하였고, 나머지 모델은 django 일반 model을 이용하여 생성하였습니다.  


- URL 구조

    /todolist/                                      - 인덱스  
    /todolist/list                                  - 할일 리스트  
    /todolist/list/`<int:category_id>`              - 할일 리스트 상세  

    /todolist/list/category/write'                  - 카테고리 작성  
    /todolist/list/`<int:category_id>`/delete       - 카테고리 삭제  
    /todolist/list/`<int:category_id>`/update       - 카테고리 수정  

    /todolist/list/`<int:category_id>`/todo/write   - 할일 작성  
    /todolist/list/todo/`<int:todo_id>`/delete      - 할일 삭제  
    /todolist/list/todo/`<int:todo_id>`/update      - 할일 수정  
    /todolist/list/todo/`<int:todo_id>`/toggle      - 할일 완료여부 토글  

    /user/login                                     - 로그인  
    /user/signup                                    - 회원가입  


- 회원기능

    우선 user/forms.py에 LoginForm과 SignUpForm을 작성했습니다. 최초에는 Modelform을 이용했으나, 로그인 과정에서 username의 유일성을 판별하는 메서드가 작동하는 부분이 불편하여, 일반 form을 사용한 후 view단에서 유효성을 검증하도록 하였고, 회원가입 부분에서는 clean 메서드를 재정의하여 username의 유일성과, 입력받은 비밀번호 두개의 동일성을 판별하도록 하였습니다.  

    view에서는 일반 클래스 view를 이용하여 Login과 SignUp을 각각 생성하고, 내부에 get과 post 요청에 따른 처리를 하도록 구성하였습니다.  
    Login 에서는 get 요청일시 render 메서드를 통해서 login.html 템플릿에 LoginForm을 context로 전달헤 줘서 렌더링 한후 반환하도록 하였습니다. 이 때, 이미 로그인 된 유저일 경우, 할일 리스트페이지로 리다이렉트 되도록 설정하였습니다. post 부분에서는 user 모델을 AbstractUser를 상속받아서 만들었으므로, django.contrib.auth의 authenticate, login를 이용하여 로그인 기능이 작동하게 만들고, 이 과정이 실패할 시 django.contrib의 message 메서드를 이용하여 에러 메세지를 생성한 후 로그인페이지로 다시 redirect 시켜서 에러 메세지를 표기하도록 하였습니다.  

    SignUp에서는 login 과 같은 방식으로 get요청을 작성하였고, post요청에서는 SignUpForm을 작성할 때 아이디의 존재여부와 입력받은 두 비밀번호가 같은지 확인하도록 했으므로, 받은 form이 valid 한지 확인한 후 정상적이라면 새로운 user를 생성하고, login 페이지로 redirect 시켰고, 정상적이지 않다면 form.non_field_errors()와 message 메서드를 이용해서 에러 메세지를 생성한 후 다시 회원가입 페이지로 redirect 시켜서, 에러 메세지를 표기하도록 하였습니다

- 할 일 관리 기능

    작성중

- 템플릿

    작성중


## 개발후기  
작성중
# common_blog

위 프로그램은 django로 제작되었습니다. 게시글과 그림을 올릴 수 있고 댓글을 올리고 지울 수 있게 만들었습니다. 관리자 아이디는 mysite 비밀번호는 mysite 입니다.

구현한 내용

-게시물(제목, 텍스트, 그림 올리기)

-메인 게시판. 게시물들의 이름을 불러옴

-댓글 기능(닉네임. 댓글 내용. 비밀번호. 댓글을 올린 시각. 삭제 기능)


프로그램을 실행시키기 위한 전제조건 python 설치. pip 설치. cmd에서 pip과 python을 실행시킬 수 있어야 함.

가상환경은 venv를 사용한다.

cmd 창 이용함.

pip install venv로 virtualenv 다운로드

cmd path를 가상환경을 생성했으면 하는 경로 에 두고 ex)'cd C:\Users\username\Documents' python -m venv [원하는 가상환경 이름] 으로 가상환경 생성

[원하는 가상환경 이름]\scripts\activate 를 쳐서 가상환경을 적용

이 아래부터는 cmd에서 가상환경이 적용되 있는 상태에서 진행.

cmd에서 다운받은 requirements.text 파일의 위치로 간 후 'pip install -r requirements.txt'실행으로 가상환경에 requirements.text에 적혀있는 환경을 적용한 가상환경에 설치한다.

다운로드한 파일에 manage.py를 찾는다.

manage.py 가 있는 경로에 cmd경로를 이동한 후 python manage.py runserver를 입력한다.

cmd창에서

System check identified no issues (0 silenced). July 04, 2021 - 10:39:32 Django version 3.2, using settings 'mysite.settings' Starting development server at http://127.0.0.1:8000/ Quit the server with CTRL-BREAK.

와 같은 메시지가 뜨면 성공. 그러면 밑줄 그어진 http://127.0.0.1:8000/를 쳐서 브라우저에서 검색해 볼 수 있다.

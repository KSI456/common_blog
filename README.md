# common_blog

위 프로그램은 django로 제작되었습니다. 게시글과 그림을 올릴 수 있고 댓글을 올리고 지울 수 있게 만들었습니다. 관리자 아이디는 mysite 비밀번호는 mysite 입니다.

구현한 내용

-게시물(제목, 텍스트, 그림 올리기)

-메인 게시판. 게시물들의 이름을 불러옴

-댓글 기능(닉네임. 댓글 내용. 비밀번호. 댓글을 올린 시각. 삭제 기능)


프로그램을 실행시키기 위한 전제조건 python 설치. pip 설치. cmd에서 pip과 python을 실행시킬 수 있어야 함.

가상환경은 venv를 사용했습니다.

cmd 창 이용함.

pip venv로 venv 다운로드

python -m venv [원하는 가상환경 이름] 으로 가상환경 생성

[원하는 가상환경 이름]\scripts\activate 를 쳐서 가상환경을 적용

cmd에서 다운받은 경로에 간 후(window의 경우 cd [경로 붙여넣기]) pip install -r requirements.txt

manage.py 가 있는 경로에 cmd경로를 이동한 후 python manage.py runserver를 입력합니다.

cmd창에서

System check identified no issues (0 silenced). July 04, 2021 - 10:39:32 Django version 3.2, using settings 'mysite.settings' Starting development server at http://127.0.0.1:8000/ Quit the server with CTRL-BREAK.

와 같은 메시지가 뜰 것입니다. 그러면 밑줄 그어진 http://127.0.0.1:8000/를 쳐서 브라우저에서 검색해 볼 수 있습니다.

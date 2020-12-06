# N 행시 API 서버

[N 행시](https://github.com/react-sprint/N_Hang_Si) 서비스를 위한 API 서버입니다.

# version

Python3 `3.8.6`  
Django `3.1.3`

# 사용법

[Python 설치 및 가상환경 사용법](https://jeongnaehyeok.github.io/python/2020/07/06/%EC%9E%A5%EA%B3%A0-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/)

## 설정

`nhangsi` 폴더 안에 `.env` 생성

```vim
DEBUG=on
DJANGO_SECRET_KEY='방구석 호랑이 문의'
N_HANG_SI_API_KEY='방구석 호랑이 문의'
```

## 실행

```bash
# 패키지 설치
$ pip install -r requirements.txt
# 마이그래이션
$ python manage.py makemigrations
$ python manage.py migrate
# 실행
$ python manage.py runserver 127.0.0.1:8000
```

## API 정리 문서

### [N 행시 API 정리 문서](https://docs.google.com/document/d/1Gn1fWumC4L1rv0BQ3Tg-pfp-Ne0nGfnJ_7rts5jl8H4/edit?usp=sharing)

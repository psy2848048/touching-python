=====================
Touching REST Client
=====================

Python 사용자를 위한 터칭 REST API 연동 모듈입니다.

* 이용 중 발생한 문제에 대해 책임지지 않습니다.

설치
=======

그냥 다운받으셔서 touching 폴더를 복사하세요...쿨럭
아직 pip에 못 올렸습니다..

기능
======
1. 해당 사용자의 포인트 정보 확인


사용법
=======

준비
------

사용하기 위해 객체를 만듭니다.

.. code-block:: python

    from touching import Touching

    # 객체 생성법
    touching = Touching('{Access-Token}', is_production={True/False})


개별 사용자 포인트 조회
------

사용자의 핸드폰 번호를 통하여 포인트 정보를 조회합니다.

.. code-block:: python

    # 상품 아이디로 조회
    response = touching.check_point('{전화번호}')



할 일
======
- 결제 목록 읽기
- 비인증 결제 세부 기능 지원
- 문서화
- 기타 등등

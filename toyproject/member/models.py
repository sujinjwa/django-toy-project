from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractUser 불러오기
# AbstractUser = django에서 기본적으로 제공하는 로그인 기능
# 기본적인 user model 또한 제공(기본 칼럼: id, username, first_name, last_name, email, password, ...)
# settings에 AUTH_USER_MODEL = 'member.Member'를 작성하여 따로 user model 작성했음을 django에 알려줘야 한다

# Create your models here.
class Member(AbstractUser):
    # AbstractUser를 통해 password, username 생략 가능
    # password = models.CharField(max_length=255, verbose_name='비밀번호')
    # username = models.CharField(max_length=128, verbose_name='이름')
    user_id = models.CharField(max_length=128, unique=True, blank=True, verbose_name='아이디')
    age = models.IntegerField(verbose_name='나이', null=True)
    status = models.CharField(max_length=16, default='일반',
        choices = (
            ('일반', '일반'),
            ('탈퇴', '탈퇴'),
            ('휴면', '휴면'),
        )
    )

    REQUIRED_FIELDS = ['user_id']

    class Meta:
        db_table = 'shinhan_member'
        verbose_name='회원'
        verbose_name_plural = '회원'
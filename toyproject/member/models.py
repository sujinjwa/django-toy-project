from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
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
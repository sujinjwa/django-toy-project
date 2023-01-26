from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Too short password')
        # 유효성 검사가 끝난 값 반환
        return make_password(value)

    class Meta:
        model = Member
        fields = ('id', 'username', 'user_id', 'password', 'age')
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'password': {
                'write_only': True,
            }
        }
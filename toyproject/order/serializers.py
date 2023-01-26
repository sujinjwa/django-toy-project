from rest_framework import serializers
from .models import Order, Comment

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )

    def get_member_username(self, obj):
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer): # 댓글을 생성하기 위한 serializer
    # model에서 member 필드를 hidden field 로 설정
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), # CurrentUserDefault : 사용자 정보를 기본값으로 바로 들어가게 설정
        required=False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value
    
    class Meta:
        model = Comment
        fields = '__all__'
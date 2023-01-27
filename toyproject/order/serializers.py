from rest_framework import serializers
from .models import Order, Comment, Like

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # SerializerMethodField (읽기 전용 필드)
    # : 모델에 없는 필드를 JSON에 추가해주거나,
    # 모델에 있는 필드를 변경해서 JSON으로 내려줄 때 사용
    like_count = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )

    def get_like_count(self, obj):
        return obj.like_set.all().count()

    def get_member_username(self, obj): # self=serializer, obj=모델 객체?
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer): # 댓글을 생성하기 위한 serializer
    # model에서 member 필드를 hidden field 로 설정
    # HiddenField: 
    member = serializers.HiddenField(
        # default(기본)값을 설정하면 필드가 필요하지 않음을 의미(required=False)
        default=serializers.CurrentUserDefault(), # CurrentUserDefault : 사용자 정보를 기본값으로 바로 들어가게 설정
        required=False
    )

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )

    class Meta:
        model = Like
        fields = '__all__'
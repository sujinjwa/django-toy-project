from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import check_password, make_password
from .models import Member
from .serializers import MemberSerializer

# Create your views here.
class MemberJoinView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ChangePasswordView(APIView):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated] # 로그인한 사용자만 들어올 수 있는 곳(request.user 들어있음)

    def put(self, request, *args, **kwargs):
        # user_id = request.data.get('user_id') -> request.user 있으므로 생략 가능
        password = request.data.get('password')
        changed_password = request.data.get('changed_password')
        changed_password2 = request.data.get('changed_password2')

        if changed_password != changed_password2:
            return Response({
                'detail': 'Wrong new password',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # if not Member.objects.filter(username=username).exists():
        #     return Response({
        #         'detail': 'No account',
        #     }, status=status.HTTP_404_NOT_FOUND)
        
        # member = Member.objects.get(username=username) -> 이미 request.user 가지고 있으므로 생략 가능
        member = request.user
        if not check_password(password, member.password):
            return Response({
                'detail': 'Wrong password',
            }, status=status.HTTP_400_BAD_REQUEST)

        member.password = make_password(changed_password)
        member.save()

        return Response(status=status.HTTP_206_PARTIAL_CONTENT)
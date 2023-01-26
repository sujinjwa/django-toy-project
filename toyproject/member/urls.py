from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberJoinView.as_view()),
    path('/password', views.ChangePasswordView.as_view()),
]
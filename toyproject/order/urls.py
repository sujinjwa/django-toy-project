from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view()),
    path('/<int:pk>', views.OrderDetailView.as_view()),
    path('/<int:pk>/comments', views.CommentListView.as_view()),
    path('/<int:pk>/comments/write', views.CommentCreateView.as_view()),
    path('/<int:order_id>/comments/<int:pk>/delete', views.CommentDeleteView.as_view()),
]
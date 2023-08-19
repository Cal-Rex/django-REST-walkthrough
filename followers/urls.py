from django.urls import path
from followers import views

urlpatterns = [
    path('follows/', views.FollowerList.as_view()),
    path('follows/<int:pk>/', views.FollowerDetail.as_view()),
]
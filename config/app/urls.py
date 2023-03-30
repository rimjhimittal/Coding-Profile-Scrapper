
from django.urls import path
from . import views

urlpatterns =[
    path('register/', views.register.as_view()),
    path('register_leetcode/', views.register_leetcode.as_view()),
    path('login/', views.login.as_view()),
    path('getLeetcodeInfo/', views.getLeetcodeInfo.as_view()),
    # path('home/', views.show_rooms.as_view()),
    
]
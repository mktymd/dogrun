from django.urls import path
from . import views


app_name = 'dogruns'
urlpatterns = [
    path('<int:pk>/edit/',views.ProfileUpdateView.as_view(),name='profile_form'),
    path('mypage/<int:pk>/',views.MyPageView.as_view(),name='mypage'),
    path('',views.DogRunListView.as_view(),name='index'),
    
    ]
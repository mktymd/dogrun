from django.urls import path
from . import views


app_name = 'dogruns'
urlpatterns = [
    path('<int:pk>/edit/',views.ProfileUpdateView.as_view(),name='profile_form'),
    path('',views.DogRunListView.as_view(),name='index'),
    path("mypage/<int:pk>/",views.MyPage.as_view(),name="mypage"),
    path("dogruns/", views.dogrun_list, name="dogrun_list"),
    path("dogruns/<int:pk>/", views.dogrun_detail, name="dogrun_detail"),
    ]


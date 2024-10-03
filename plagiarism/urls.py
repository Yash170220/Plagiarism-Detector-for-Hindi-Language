from django.urls import path
from plagiarism import views

urlpatterns=[
    path('',views.home,name='plagiarism-check-mainpage'),
    path('check',views.checker,name='check'),
]
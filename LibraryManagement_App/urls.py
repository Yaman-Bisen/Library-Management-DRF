from django.urls import path
from .views import *
urlpatterns = [
    path('',index),
    path('admin_login/',admin_login,name="admin_login"),
    path('student_login/',student_login,name="student_login"),
    path('student_signup/',student_signup,name="student_signup"),
    path('admin_dashboard/',admin_dashboard,name="admin_dashboard"),
    path('student_dashboard/',student_dashboard,name="student_dashboard"),
]

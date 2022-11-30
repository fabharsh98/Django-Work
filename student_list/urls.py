from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("student_list/", views.stud_list, name='stud_list'),
    path("student_register/", views.stud_reg, name='stud_reg'),
    path("student_edit/<int:id>/", views.stud_reg, name='stud_edit'),
    path("student_delete/<int:id>", views.stud_del, name='stud_del'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('subject/add/', views.add_subject, name='add_subject'),
    path('teachers/edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/filter/', views.filter_teachers, name='filter_teachers'),
    path('teachers/import/', views.import_teachers, name='import_teachers'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
]

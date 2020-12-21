from django.urls import path


from . import views

app_name = 'home'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('login/', views.login, name='login'),
    path('edit/', views.edit, name='edit'),
]
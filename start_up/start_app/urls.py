from django.urls import path
from start_app import views

#TEMPLATE TAGGING
app_name = 'start_app'

urlpatterns = [
    path('other/', views.other, name = 'other'),
    path('relative/', views.relative, name = 'relative'),
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.user_login, name = 'login')
]

from django.urls import path
from accounts.views import user_login, register_user, user_logout


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
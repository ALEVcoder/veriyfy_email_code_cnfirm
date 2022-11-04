from django.urls import path
from .views import register, log_out, log_in, index, verify, resend_code

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('verify/<int:id>/', verify, name='verify'),
    path('resend/<int:id>/', resend_code, name='resend'),
    path('login/', log_in, name='login'),
    path('log_out/', log_out, name='log_out'),
]
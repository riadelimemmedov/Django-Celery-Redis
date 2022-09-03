from django.urls import path
from .views import  *

app_name='mainapp'
urlpatterns = [
    path('',test,name='test'),
    path('send-email/',send_email_to_all_users,name='sendemail')
]

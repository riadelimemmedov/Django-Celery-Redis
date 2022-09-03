from django.shortcuts import render,HttpResponse
from .tasks import *

from email_send.tasks import send_email_func

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse('Done')


def send_email_to_all_users(request):
    send_email_func.delay()
    return HttpResponse('Successfully Sending Discount Message,All Subscribes Recipents')


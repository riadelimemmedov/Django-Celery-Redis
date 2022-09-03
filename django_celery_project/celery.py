from  __future__  import absolute_import,unicode_literals
import os
from time import timezone

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Baku')

app.config_from_object(settings, namespace='CELERY')

#!Celery Beat Settings
app.conf.beat_schedule = {
    
    #?If you are sending every 30 secons sending email use this object
    'send-email-all-users':{
        'task':'send_email_repatly',
        'schedule':30.0
    }
    
    #?If you are sending email special minute use crontab
    # 'send-email-all-users':{
    #     'task':'send_email_repatly',
    #     'schedule':crontab(hour=0,minute=45,day_of_month=19,month_of_year=6)#?This function constantly sending emails every 45 minute 
    # }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
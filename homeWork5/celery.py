import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homeWork5.settings')

app = Celery('homeWork5', include=[])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, name='celery')
def test_task(self):
    return 'it works)'

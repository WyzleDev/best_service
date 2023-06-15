from .models import WeekSchedule
from tasks.celery_config import app as celery_app

from celery.schedules import crontab


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=17, minute=43, day_of_week=1)
    ),
    create_new_week.s()


@celery_app.task(bind=True)
def create_new_week():
    last_week_number = WeekSchedule.objects.last()
    last_week_number = int(last_week_number.id)
    new_obj = WeekSchedule.objects.create(week_number=last_week_number + 1)
    new_obj.save()

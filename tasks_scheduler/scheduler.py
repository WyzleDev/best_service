import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys

from groups.models import StudentGroup
from schedule_models.models_updated import CurrentWeek
from schedule_models.models import DaySchedule
from apscheduler.triggers.cron import CronTrigger


def create_current_week():
    year, week_number, day_of_week = datetime.datetime.now().isocalendar()
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    daterange = [start_week + datetime.timedelta(days=x) for x in range(0, (end_week - start_week).days)]
    groups_list = list(StudentGroup.objects.all())
    for group in groups_list:
        curr_week = CurrentWeek.objects.create(week_number=week_number, group=group)
        for date in daterange:
            day = DaySchedule.objects.create(date=f'{date}', day_of_week=day_of_week, group=group)
        days = DaySchedule.objects.filter(group=group)
        for day in days:
            curr_week.days.add(day)



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every sunday
    scheduler.add_job(create_current_week, CronTrigger(day_of_week="sat", minute=1), name='new_week', jobstore='default')
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)

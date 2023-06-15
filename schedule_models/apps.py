from django.apps import AppConfig


class ScheduleModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule_models'

    def ready(self):
        from tasks_scheduler import scheduler
        scheduler.start()

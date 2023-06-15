from django.urls import path

from . import views

urlpatterns = [
    # GET urls
    path('teacher/<teacher_id>/', view=views.TeacherViewSet.as_view(), name='teacher'),
    path('lesson/<lesson_id>/', view=views.ExactLessonViewSet.as_view(), name='lesson'),
    path('student/<student_id>/', view=views.StudentViewSet.as_view(), name='student'),
    path('group/<name>/', view=views.GroupViewSet.as_view(), name='group'),
    path('daySchedule/<day_id>', view=views.DayScheduleViewSet.as_view(), name='day'),
    path('news/', views.PostViewSet.as_view(), name='news'),
    path('news/<id>', view=views.ExactPostViewSet.as_view(), name='exact_post'),
    path("current_weeek/<group>/", views.CurrentWeekViewSet.as_view(), name='current_week'),
    path('groups/', view = views.AllGroupsViewSet.as_view(), name='all_groups'),
    path('events/', view=views.EventsViewSet.as_view(), name="events"),
    path("events/<id>", view=views.ExactEventViewSet.as_view(), name='exact view'),


    # POST urls
    path('student/create', view=views.CreateUser.as_view(), name='create_user'),
    

    # PUT urls
]

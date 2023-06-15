import datetime
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import Post
# importing custom models
from users.models import CustomUser
from groups.models import StudentGroup
from schedule_models.models import Teacher, Lesson, DaySchedule
from events.models import Event

# importing custom serializers
from .serializers import TeacherSerializer, LessonSerializer, StudentSerializer, \
    GroupSerializer, \
    DayScheduleSerializer, PostSerializer, CurrentWeekSerializer, ExactPostSerializer, EventSerializer

from schedule_models.models_updated import CurrentWeek

#
class TeacherViewSet(APIView):
    @staticmethod
    def get(request, teacher_id: int):
        teacher = Teacher.objects.filter(id=teacher_id)
        serializer_data = {
            "request": request
        }
        serializer = TeacherSerializer(teacher, many=True, context=serializer_data)
        return Response(serializer.data)


# 
class ExactLessonViewSet(APIView):
    @staticmethod
    def get(request, lesson_id: int):
        lesson = Lesson.objects.filter(id=lesson_id)
        serializer_data = {
            "request": request
        }
        serializer = LessonSerializer(lesson, many=True, context=serializer_data)
        return Response(serializer.data)


# 
class StudentViewSet(APIView):
    @staticmethod
    def get(request, student_id: int):
        student = CustomUser.objects.filter(id=student_id)
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)


# 
class GroupViewSet(APIView):
    @staticmethod
    def get(request, name: str):
        group = StudentGroup.objects.filter(name=name)
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)

class AllGroupsViewSet(APIView):
    @staticmethod
    def get(request):
        groups = StudentGroup.objects.all()
        serializer = GroupSerializer(groups, many = True)
        return Response(serializer.data)


# 
class DayScheduleViewSet(APIView):
    @staticmethod
    def get(request, day_id: int):
        day_schedule = DaySchedule.objects.filter(id=day_id)
        serializer = DayScheduleSerializer(day_schedule)
        return Response(serializer.data)


# 
class CreateUser(APIView):
    @staticmethod
    def post(request):
        serialized = StudentSerializer(data=request.data)
        if serialized.is_valid():
            CustomUser.objects.create_user(
                username=serialized.initial_data['username'],
                email=serialized.initial_data['email'],
                password=serialized.initial_data['password'],
                birth_date=serialized.initial_data['birth_date'],
                course=serialized.initial_data['course'],
                avatar=serialized.initial_data['avatar']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(APIView):
    @staticmethod
    def get(request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class ExactPostViewSet(APIView):
    @staticmethod
    def get(request, id):
        post = Post.objects.filter(id=int(id))
        serializer = ExactPostSerializer(post, many=True)
        return Response(serializer.data)

class CurrentWeekViewSet(APIView):
    def get(self, request, group):
        curr_week = CurrentWeek.objects.get(group__name = group)
        serializer = CurrentWeekSerializer(curr_week)
        return Response(serializer.data)


class EventsViewSet(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class ExactEventViewSet(APIView):
    def get(self, request, id):
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
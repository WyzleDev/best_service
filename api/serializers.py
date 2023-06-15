from rest_framework import serializers
from groups.models import StudentGroup
from news.models import Post
from schedule_models.models import Teacher, Lesson, DaySchedule
from users.models import CustomUser
from schedule_models.models_updated import CurrentWeek
from events.models import EventTag, Event


class TeacherSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    bio = serializers.StringRelatedField()

    class Meta:
        model = Teacher
        fields = ['id', 'avatar', 'first_name', 'last_name', 'bio']


class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    avatar = serializers.ImageField(use_url=True)
    name = serializers.CharField(read_only=True)
    teacher = TeacherSerializer(many=True)
    description = serializers.StringRelatedField()

    class Meta:
        model = Lesson
        fields = "__all__"


class StudentSerializer(serializers.Serializer):
    avatar = serializers.ImageField(use_url=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    course = serializers.IntegerField()
    birth_date = serializers.DateField()

    class Meta:
        model = CustomUser


class GroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    course = serializers.IntegerField()
    students = StudentSerializer(many=True)

    class Meta:
        model = StudentGroup


class DayScheduleSerializer(serializers.Serializer):
    date = serializers.CharField()
    day_of_week = serializers.CharField()
    group = GroupSerializer()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = DaySchedule

class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    header = serializers.CharField()
    body = serializers.StringRelatedField()
    created = serializers.DateField()

    class Meta:
        model = Post
        exclude = ['updated']

class ExactPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['updated']

class CurrentWeekSerializer(serializers.ModelSerializer):
    week_number = serializers.IntegerField()
    days = DayScheduleSerializer(many=True)
    group = serializers.CharField()

    class Meta:
        model = CurrentWeek
        exclude = ["id"]

class EventTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTag
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField()
    header = serializers.CharField()
    event_tags = EventTagSerializer(many=True)
    date = serializers.DateTimeField()
    location = serializers.StringRelatedField()
    participants = StudentSerializer(many=True)
    description = serializers.StringRelatedField()
    social_link1 = serializers.URLField()
    social_link2 = serializers.URLField()
    class Meta:
        model = Event
        fields = "__all__"

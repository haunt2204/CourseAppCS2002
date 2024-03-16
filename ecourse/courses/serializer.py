from .models import Category, Course, Lesson, Tag
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        model = Course
        fields = '__all__'
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Category, Course, Tag, Lesson
from .serializer import CategorySerializer, CourseSerializer
from .paginator import CoursePaginator

# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course,CourseSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet,ModelViewSet



# Create your views here.
#for modelviewset
class CourseViewSet(ModelViewSet):
    queryset= Course.objects.all()
    serializer_class=CourseSerializer

'''
# for view set
class CourseViewSet(ViewSet):
    def list(self,request):
        courses = Course.objects.all()
        serializer= CourseSerializer(courses,many= True)
        return Response(serializer.data)

    def create(self,request):
        serializer= CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.data)

    def retrieve(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer= CourseSerializer(course)
        return Response(serializer.data)
'''

# combination of ListModelMixin & GenericAPIView is ListAPIView


'''
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer

class CourseDetilesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer
'''
'''
#for mixin,and generics
class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class CourseDetailView(generics.GenericAPIView):
    pass
'''


'''

class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
    #post 

    def post(self,request):
        courseSerializer=CourseSerializer(data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data,status=status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)

'''


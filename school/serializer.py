from rest_framework import serializers
from school.models import Student, Course
#from school.serializer import StudentSerializer, CourseSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

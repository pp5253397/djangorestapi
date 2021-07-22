from rest_framework import serializers
from .models import Student,Teacher,Lecture

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True, read_only=True)



    class Meta:
        model = Lecture
        fields = '__all__'
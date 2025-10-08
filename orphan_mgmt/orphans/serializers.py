# Orphans serializers

from rest_framework import serializers
from .models import Orphan, Course

class OrphanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orphan
        fields = '__all__' # include all fields
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
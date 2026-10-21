from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

    Serializes the fields: 'id', 'name', 'html', 'css', and 'js' for
    input/output operations via Django REST Framework.
    """
    class Meta:
        model = Project
        fields = ['id', 'name', 'html', 'css', 'js']

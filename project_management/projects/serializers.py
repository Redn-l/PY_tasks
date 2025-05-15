from rest_framework import serializers
from .models import Project, Task
from .dto import ProjectDTO, TaskDTO

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        dto = ProjectDTO(instance.id, instance.name, instance.description)
        return {
            'id': dto.id,
            'name': dto.name,
            'description': dto.description,
        }

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        dto = TaskDTO(
            id=instance.id,
            title=instance.title,
            description=instance.description,
            status=instance.status,
            project_id=instance.project.id
        )
        return {
            'id': dto.id,
            'title': dto.title,
            'description': dto.description,
            'status': dto.status,
            'project': dto.project_id
        }

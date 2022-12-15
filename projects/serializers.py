from rest_framework import serializers
from .models import Project,Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Project
        fields = '__all__'

    def get_tags(self, obj):
        tags = obj.tag.values('name')
        serializers = TagSerializer(tags, many = True)
        return serializers.data
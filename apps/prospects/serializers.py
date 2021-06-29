from rest_framework.serializers import ModelSerializer

from rest_framework.serializers import ModelSerializer
from .models import Skills


class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"

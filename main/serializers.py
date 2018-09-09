from rest_framework.serializers import ModelSerializer

from main.models import File

class FileSerializer(ModelSerializer):
    class Meta:
        model=File
        fields=('author','title')

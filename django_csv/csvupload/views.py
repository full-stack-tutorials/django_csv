from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from csvupload.models import CSVModel

class CSVUploadSerializer(ModelSerializer):
    class Meta:
        model = CSVModel
        fields = ('csv_file', 'csv_filename')

class CSVUploadViewSet(ModelViewSet):
    queryset = CSVModel.objects.all()
    serializer_class = CSVUploadSerializer
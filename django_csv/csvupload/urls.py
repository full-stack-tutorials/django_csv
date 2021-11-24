from csvupload import views as csvupload_views
from django.urls import path

urlpatterns = [
    path(r'csv-upload/', csvupload_views.CSVUploadViewSet.as_view({'get': 'list', 'post': 'create'}), name='csv-upload'),
]
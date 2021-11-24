from csvupload import urls as csvupload_urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('csvupload.urls')),
]

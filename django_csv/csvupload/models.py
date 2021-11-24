import uuid

from django.db import models

class CSVModel(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(upload_to='csv_files')
    csv_filename = models.CharField(max_length=1024, db_index=True, unique=True)

    def __str__(self) -> str:
        return f'CSVModel: {self.csv_filename}'
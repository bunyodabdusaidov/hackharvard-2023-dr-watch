from django.db import models
import uuid
from datetime import datetime, timedelta

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=50)
    age=models.IntegerField
    gender=models.CharField
    date_of_birth=models.CharField
    last_visit_date=models.DateTimeField(auto_now_add=True)
    next_visit_date=models.DateTimeField(default=datetime.now() + timedelta(days=30))

    class Meta:
        app_label = 'patient'

    def __str__(self):
        return self.id
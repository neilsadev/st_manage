import uuid
from django.db import models
from institute.models import *

class Student(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    department = models.ForeignKey(Department, related_name='students', on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length = 50)
    birthyear = models.IntegerField()
    address = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True, editable = False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
import uuid
from django.db import models

DEGREE = (
    ('science', 'B.Sc'),
    ('commerce', 'B.BA'),
    ('arts', 'B.A'),
)

class Department(models.Model):
    name = models.CharField(max_length = 255)
    degree = models.CharField(max_length = 255, choices=DEGREE, default='waiscienceting')

    def __str__(self):
        return f"{self.degree} in {self.name} offered at {self.institute}"

class Institute(models.Model):
    name = models.CharField(max_length = 200)
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    year = models.IntegerField()
    address = models.CharField(max_length = 500)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable = False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} established in {self.year}"

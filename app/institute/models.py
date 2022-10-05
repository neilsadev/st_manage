import uuid
from django.db import models

DEGREE = (
    ('science', 'B.Sc'),
    ('commerce', 'B.BA'),
    ('arts', 'B.A'),
)

class Institute(models.Model):
    name = models.CharField(max_length = 200)
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    year = models.IntegerField()
    address = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True, editable = False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return f"{self.name} established in {self.year}"

class Department(models.Model):
    name = models.CharField(max_length = 255)
    degree = models.CharField(max_length = 255, choices=DEGREE, default='science')
    institute = models.ForeignKey(Institute, related_name='departments', on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return f"{self.degree} in {self.name} offered at {self.institute}"

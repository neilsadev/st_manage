import uuid
from django.db import models

# class B(models.Model):
#     y=models.CharField(max_length=255)


class Institute(models.Model):
    name = models.CharField(max_length = 200)
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    year = models.IntegerField()
    address = models.CharField(max_length = 500)
    # b=models.ForeignKey(B,null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable = False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} established in {self.year}"



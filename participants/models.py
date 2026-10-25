import uuid
from django.db import models


class Participant(models.Model):
    id = models.CharField(
        primary_key=True, 
        max_length=8, 
        default=uuid.uuid4, 
        editable=False
    )
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email")
    role = models.CharField(max_length=100, verbose_name="Роль")

    def __str__(self):
        return f"{self.full_name} ({self.role})"
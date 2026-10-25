import uuid
from django.db import models
from participants.models import Participant


class Event(models.Model):
    id = models.CharField(primary_key=True, max_length=8, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name="Название")
    date = models.DateField(verbose_name="Дата проведения")
    location = models.CharField(max_length=200, verbose_name="Место проведения")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

class Album(models.Model):
    id = models.CharField(primary_key=True, max_length=8, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name="Название альбома")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f"{self.title} ({self.event.title})"

class Photo(models.Model):
    id = models.CharField(primary_key=True, max_length=8, default=uuid.uuid4, editable=False)
    file_url = models.URLField(verbose_name="Ссылка на файл")
    resolution = models.CharField(max_length=50, verbose_name="Разрешение")
    upload_date = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    participants = models.ManyToManyField(Participant, blank=True, related_name='photos')

    def __str__(self):
        return f"Фото {self.id} ({self.resolution})"
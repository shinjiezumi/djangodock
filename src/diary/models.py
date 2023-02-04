from django.db import models
from django.utils import timezone  # Djangoでは datetime.now の代わりに、 timezone.now で現在日時を取得する


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
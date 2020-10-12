from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  # 복사 붙여넣기를 방지하기 위함

    class Meta:
        abstract = True
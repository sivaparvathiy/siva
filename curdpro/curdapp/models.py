from django.db import models

class curdData(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField()
    relation=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    professional=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)

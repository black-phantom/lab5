from django.db import models

class rasp(models.Model):
    day = models.CharField(max_length=200)
    subj = models.CharField(max_length=200)
	group = models.CharField(max_length=200)
	facl = models.CharField(max_length=200)



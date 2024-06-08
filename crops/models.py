from django.contrib.auth.models import User
from django.db import models


class CropHistory(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph_level = models.FloatField()
    rainfall = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    predication = models.CharField(max_length=360, null=True, blank=True)

    class Meta:
        verbose_name = "Crop History"
        verbose_name_plural = "Crop Histories"

    def __str__(self):
        return self.user.username


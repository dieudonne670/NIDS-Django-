from django.db import models


class Anomaly(models.Model):

    source_ip = models.CharField(max_length=100)

    destination_ip = models.CharField(max_length=100)

    protocol = models.CharField(max_length=20)

    packet_size = models.IntegerField()

    anomaly_score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_ip} - {self.anomaly_score}"
# Create your models here.

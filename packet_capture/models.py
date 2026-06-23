from django.db import models


class TrafficLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()

    protocol = models.CharField(max_length=20)

    source_port = models.IntegerField(null=True, blank=True)
    destination_port = models.IntegerField(null=True, blank=True)

    packet_size = models.IntegerField()

    def __str__(self):
        return f"{self.source_ip} -> {self.destination_ip}"

# Create your models here.

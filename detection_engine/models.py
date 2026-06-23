from django.db import models


class Alert(models.Model):

    SEVERITY_CHOICES = (
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    source_ip = models.GenericIPAddressField()

    attack_type = models.CharField(max_length=50)

    severity = models.CharField(
        max_length=10,
        choices=SEVERITY_CHOICES
    )

    description = models.TextField()

    def __str__(self):
        return self.attack_type

# Create your models here.

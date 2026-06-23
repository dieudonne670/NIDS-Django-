from django.core.management.base import BaseCommand

from ml_module.anomaly_detector import (
    run_anomaly_detection
)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        run_anomaly_detection()
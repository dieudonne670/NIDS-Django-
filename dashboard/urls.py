from django.urls import path
from . import views

from dashboard.reports import (
    export_alerts_csv,
    export_alerts_pdf
)

urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "export/csv/",
        export_alerts_csv,
        name="export_csv"
    ),

    path(
        "export/pdf/",
        export_alerts_pdf,
        name="export_pdf"
    ),

    path(
    "traffic/",
    views.traffic_logs,
    name="traffic"
    ),

    path(
        "alerts/",
        views.alerts,
        name="alerts"
    ),

    path(
        "anomalies/",
        views.anomalies,
        name="anomalies"
    ),

    path(
        "reports/",
        views.reports,
        name="reports"
    ),
]



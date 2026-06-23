from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from packet_capture.models import TrafficLog
from detection_engine.models import Alert
from ml_module.models import Anomaly


def dashboard(request):

    protocol_stats = (
        TrafficLog.objects
        .values("protocol")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    top_attackers = (
        Alert.objects
        .values("source_ip")
        .annotate(total=Count("id"))
        .order_by("-total")[:5]
    )

    attack_timeline = (
    Alert.objects
    .annotate(day=TruncDate("timestamp"))
    .values("day")
    .annotate(total=Count("id"))
    .order_by("day")
)

    context = {

        "traffic_count": TrafficLog.objects.count(),

        "alert_count": Alert.objects.count(),

        "anomaly_count": Anomaly.objects.count(),

        "recent_traffic":
            TrafficLog.objects.order_by("-id")[:15],

        "recent_alerts":
            Alert.objects.order_by("-id")[:10],

        "recent_anomalies":
            Anomaly.objects.order_by("-id")[:10],

        "protocol_stats": protocol_stats,

        "top_attackers": top_attackers,
        "attack_timeline": attack_timeline,
    }

    return render(
        request,
        "dashboard/index.html",
        context
    )


def traffic_logs(request):

    traffic = TrafficLog.objects.order_by("-id")

    return render(
        request,
        "dashboard/traffic.html",
        {"traffic": traffic}
    )


def alerts(request):

    alerts = Alert.objects.order_by("-id")

    return render(
        request,
        "dashboard/alerts.html",
        {"alerts": alerts}
    )


def anomalies(request):

    anomalies = Anomaly.objects.order_by("-id")

    return render(
        request,
        "dashboard/anomalies.html",
        {"anomalies": anomalies}
    )


def reports(request):

    context = {
        "traffic_count": TrafficLog.objects.count(),
        "alert_count": Alert.objects.count(),
        "anomaly_count": Anomaly.objects.count(),
    }

    return render(
        request,
        "dashboard/reports.html",
        context
    )
# Create your views here.

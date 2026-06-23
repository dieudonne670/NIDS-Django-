import csv

from django.http import HttpResponse

from detection_engine.models import Alert


def export_alerts_csv(request):

    response = HttpResponse(
        content_type="text/csv"
    )

    response[
        "Content-Disposition"
    ] = 'attachment; filename="alerts.csv"'

    writer = csv.writer(response)

    writer.writerow([
        "Source IP",
        "Attack Type",
        "Severity",
        "Description"
    ])

    alerts = Alert.objects.all()

    for alert in alerts:

        writer.writerow([
            alert.source_ip,
            alert.attack_type,
            alert.severity,
            alert.description
        ])

    return response


from reportlab.pdfgen import canvas

from django.http import HttpResponse

from detection_engine.models import Alert


def export_alerts_pdf(request):

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = 'attachment; filename="alerts.pdf"'

    pdf = canvas.Canvas(response)

    pdf.setTitle("NIDS Report")

    pdf.drawString(
        200,
        800,
        "NIDS ALERT REPORT"
    )

    y = 760

    alerts = Alert.objects.all()

    for alert in alerts:

        line = (
            f"{alert.source_ip} | "
            f"{alert.attack_type} | "
            f"{alert.severity}"
        )

        pdf.drawString(
            50,
            y,
            line
        )

        y -= 20

        if y < 50:

            pdf.showPage()

            y = 800

    pdf.save()

    return response
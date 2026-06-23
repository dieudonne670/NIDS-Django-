import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

from packet_capture.models import TrafficLog
from ml_module.models import Anomaly


def run_anomaly_detection():

    traffic = list(TrafficLog.objects.all())

    if len(traffic) < 50:
        print("Need more traffic data")
        return

    protocol_map = {
        "TCP": 1,
        "UDP": 2,
        "ICMP": 3,
        "OTHER": 4,
    }

    data = []

    for row in traffic:

        data.append([
            row.packet_size,
            row.source_port or 0,
            row.destination_port or 0,
            protocol_map.get(row.protocol, 4),
        ])

    df = pd.DataFrame(
        data,
        columns=[
            "packet_size",
            "source_port",
            "destination_port",
            "protocol",
        ]
    )

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    model = IsolationForest(
        n_estimators=200,
        contamination=0.03,
        random_state=42
    )

    predictions = model.fit_predict(scaled_data)

    scores = model.decision_function(scaled_data)

    # Optional: clear old anomalies before inserting new ones
    Anomaly.objects.all().delete()

    for traffic_log, prediction, score in zip(
        traffic,
        predictions,
        scores
    ):

        if prediction == -1:

            Anomaly.objects.create(
                source_ip=traffic_log.source_ip,
                destination_ip=traffic_log.destination_ip,
                protocol=traffic_log.protocol,
                packet_size=traffic_log.packet_size,
                anomaly_score=float(score)
            )

    print("Anomaly Detection Completed")
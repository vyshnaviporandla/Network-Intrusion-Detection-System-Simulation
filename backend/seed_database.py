import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import init_db, process


CSV_FILE = ROOT / "data" / "network_traffic.csv"


def main():
    if not CSV_FILE.exists():
        print(f"Dataset not found: {CSV_FILE}")
        return

    init_db()

    processed = 0
    alerts = 0

    print("Loading synthetic network traffic...")
    print(f"Dataset: {CSV_FILE}")

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            flow = {
                "flow_id": row["flow_id"],
                "timestamp": row["timestamp"],
                "source_ip": row["source_ip"],
                "destination_ip": row["destination_ip"],
                "source_port": int(row["source_port"]),
                "destination_port": int(row["destination_port"]),
                "protocol": row["protocol"],
                "packet_count": int(row["packet_count"]),
                "byte_count": int(row["byte_count"]),
                "duration_seconds": float(row["duration_seconds"]),
                "connection_count": int(row["connection_count"]),
                "failed_connection_count": int(row["failed_connection_count"]),
                "syn_count": int(row["syn_count"]),
                "rst_count": int(row["rst_count"]),
                "average_packet_size": float(row["average_packet_size"]),
                "label": row["label"],
                "scenario_type": row["scenario_type"],
            }

            _, alert = process(flow)

            processed += 1

            if alert:
                alerts += 1

            if processed % 500 == 0:
                print(
                    f"Processed {processed} flows | "
                    f"Alerts generated: {alerts}"
                )

    print()
    print("========================================")
    print("DATABASE SEEDING COMPLETE")
    print("========================================")
    print(f"Flows processed : {processed}")
    print(f"Alerts generated: {alerts}")
    print("Database        : data\\ids.db")
    print("========================================")


if __name__ == "__main__":
    main()
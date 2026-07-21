import pandas as pd

from services.user_data_service import (
    load_processed_data
)


class VisualizationAgent:

    def __init__(self, user_id):

        self.df = load_processed_data(
            user_id
        )

        if self.df is None:
            raise Exception(
                "No processed dataset found"
            )

        self.latest_df = (
            self.df
            .sort_values("cycle")
            .groupby("engine_id")
            .tail(1)
        )

    # -----------------------------
    # Health Distribution
    # -----------------------------

    def health_distribution_chart(self):

        counts = (
            self.latest_df["Health_Status"]
            .value_counts()
        )

        return {
            "chart_type": "pie",
            "title": "Health Distribution",
            "data": [
                {
                    "name": status,
                    "value": int(count)
                }
                for status, count in counts.items()
            ]
        }

    # -----------------------------
    # Risk Distribution
    # -----------------------------

    def risk_distribution_chart(self):

        counts = (
            self.latest_df["Risk_Level"]
            .value_counts()
        )

        return {
            "chart_type": "pie",
            "title": "Risk Distribution",
            "data": [
                {
                    "name": risk,
                    "value": int(count)
                }
                for risk, count in counts.items()
            ]
        }

    # -----------------------------
    # Maintenance Distribution
    # -----------------------------

    def maintenance_distribution_chart(self):

        counts = (
            self.latest_df["Maintenance_Priority"]
            .value_counts()
        )

        return {
            "chart_type": "bar",
            "title": "Maintenance Distribution",
            "data": [
                {
                    "name": priority,
                    "value": int(count)
                }
                for priority, count in counts.items()
            ]
        }

    # -----------------------------
    # Fault Distribution
    # -----------------------------

    def fault_distribution_chart(self):

        counts = (
            self.latest_df["Fault_Status"]
            .value_counts()
        )

        return {
            "chart_type": "pie",
            "title": "Fault Distribution",
            "data": [
                {
                    "name": fault,
                    "value": int(count)
                }
                for fault, count in counts.items()
            ]
        }

    # -----------------------------
    # RUL Histogram
    # -----------------------------

    def rul_histogram(self):

        return {
            "chart_type": "histogram",
            "title": "RUL Distribution",
            "data": [
                float(x)
                for x in self.latest_df[
                    "Predicted_RUL"
                ].tolist()
            ]
        }
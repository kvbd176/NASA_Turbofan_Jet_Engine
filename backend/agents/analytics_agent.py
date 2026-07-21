import pandas as pd


from services.user_data_service import (
    load_processed_data
)

class AnalyticsAgent:

    def __init__(self):
        self.latest_df = None


    def get_latest_df(self, user_id):

        df = load_processed_data(
            user_id
        )

        self.latest_df = (
            df
            .sort_values("cycle")
            .groupby("engine_id")
            .tail(1)
        )

        return self.latest_df
    # ---------------------------------
    # Health Status Distribution
    # ---------------------------------
    def health_distribution(
            self,
            user_id
        ):

            latest_df = self.get_latest_df(user_id)

            return (
                latest_df["Health_Status"]
                .value_counts()
                .to_dict()
            )

    # ---------------------------------
    # Risk Distribution
    # ---------------------------------
    def risk_distribution(self,user_id):
        self.get_latest_df(user_id)

        counts = (
            self.latest_df["Risk_Level"]
            .value_counts()
        )

        return [
            {
                "risk_level": risk,
                "count": int(count)
            }
            for risk, count in counts.items()
        ]

    # ---------------------------------
    # Fault Distribution
    # ---------------------------------
    def fault_distribution(self,user_id):
        self.get_latest_df(user_id)

        counts = (
            self.latest_df["Fault_Status"]
            .value_counts()
        )

        return [
            {
                "fault_status": fault,
                "count": int(count)
            }
            for fault, count in counts.items()
        ]

    # ---------------------------------
    # Maintenance Distribution
    # ---------------------------------
    def maintenance_distribution(self,user_id):
        self.get_latest_df(user_id)

        counts = (
            self.latest_df["Maintenance_Priority"]
            .value_counts()
        )

        return [
            {
                "priority": priority,
                "count": int(count)
            }
            for priority, count in counts.items()
        ]

    # ---------------------------------
    # Top Critical Engines
    # ---------------------------------
    def critical_engines(self,user_id):
        self.get_latest_df(user_id)

        critical = self.latest_df[
            self.latest_df["Health_Status"]
            == "Critical"
        ]

        critical = critical.sort_values(
            "Predicted_RUL"
        )

        return critical[
            [
                "engine_id",
                "Predicted_RUL",
                "Risk_Level"
            ]
        ].to_dict(
            orient="records"
        )

    # ---------------------------------
    # RUL Distribution
    # ---------------------------------
    def rul_distribution(self,user_id):
        self.get_latest_df(user_id)

        return self.latest_df[
            "Predicted_RUL"
        ].tolist()
import pandas as pd

from services.user_data_service import (
    load_processed_data
)


class ReportGenerationAgent:

    def get_latest_df(
        self,
        user_id
    ):

        df = load_processed_data(
            user_id
        )

        if df is None:
            return None

        latest_df = (
            df
            .sort_values("cycle")
            .groupby("engine_id")
            .tail(1)
        )

        return latest_df

    # ----------------------------------
    # System Report
    # ----------------------------------

    def generate_system_report(
        self,
        user_id
    ):

        latest_df = self.get_latest_df(
            user_id
        )

        if latest_df is None:
            return {
                "error":
                "No processed dataset found"
            }

        report = {

            "Total_Engines":
                int(
                    latest_df["engine_id"].nunique()
                ),

            "Healthy_Engines":
                int(
                    (
                        latest_df["Health_Status"]
                        == "Healthy"
                    ).sum()
                ),

            "Degrading_Engines":
                int(
                    (
                        latest_df["Health_Status"]
                        == "Degrading"
                    ).sum()
                ),

            "Critical_Engines":
                int(
                    (
                        latest_df["Health_Status"]
                        == "Critical"
                    ).sum()
                ),

            "Faulty_Engines":
                int(
                    (
                        latest_df["Fault_Status"]
                        == "Fault Detected"
                    ).sum()
                ),

            "High_Risk_Engines":
                int(
                    (
                        latest_df["Risk_Level"]
                        == "High"
                    ).sum()
                ),

            "Immediate_Maintenance_Engines":
                int(
                    (
                        latest_df["Maintenance_Priority"]
                        == "Immediate"
                    ).sum()
                ),

            "Average_RUL":
                float(
                    round(
                        latest_df["Predicted_RUL"].mean(),
                        2
                    )
                )
        }

        return report

    # ----------------------------------
    # Critical Engines Report
    # ----------------------------------

    def critical_engines_report(
        self,
        user_id
    ):

        latest_df = self.get_latest_df(
            user_id
        )

        if latest_df is None:
            return []

        critical = latest_df[
            latest_df["Health_Status"]
            == "Critical"
        ]

        return critical[
            [
                "engine_id",
                "Predicted_RUL",
                "Risk_Level",
                "Maintenance_Action"
            ]
        ].to_dict(
            orient="records"
        )

    # ----------------------------------
    # Maintenance Report
    # ----------------------------------

    def maintenance_report(
        self,
        user_id
    ):

        latest_df = self.get_latest_df(
            user_id
        )

        if latest_df is None:
            return []

        maintenance = latest_df[
            latest_df[
                "Maintenance_Priority"
            ] == "Immediate"
        ]

        return maintenance[
            [
                "engine_id",
                "Predicted_RUL",
                "Maintenance_Action"
            ]
        ].to_dict(
            orient="records"
        )

    # ----------------------------------
    # Engine Report
    # ----------------------------------

    def engine_report(
        self,
        user_id,
        engine_id
    ):

        latest_df = self.get_latest_df(
            user_id
        )

        if latest_df is None:
            return {
                "error":
                "No processed dataset found"
            }

        engine = latest_df[
            latest_df["engine_id"]
            == engine_id
        ]

        if engine.empty:

            return {
                "error":
                f"Engine {engine_id} not found"
            }

        return engine.to_dict(
            orient="records"
        )[0]
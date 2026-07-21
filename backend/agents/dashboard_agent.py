import pandas as pd


from services.user_data_service import load_processed_data


class DashboardAgent:

    def __init__(self,user_id):

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

    def get_kpis(self):

        return {

            "total_engines":
                int(self.latest_df["engine_id"].nunique()),

            "healthy_engines":
                int(
                    (
                        self.latest_df["Health_Status"]
                        == "Healthy"
                    ).sum()
                ),

            "degrading_engines":
                int(
                    (
                        self.latest_df["Health_Status"]
                        == "Degrading"
                    ).sum()
                ),

            "critical_engines":
                int(
                    (
                        self.latest_df["Health_Status"]
                        == "Critical"
                    ).sum()
                ),

            "faulty_engines":
                int(
                    (
                        self.latest_df["Fault_Status"]
                        == "Fault Detected"
                    ).sum()
                ),

            "high_risk_engines":
                int(
                    (
                        self.latest_df["Risk_Level"]
                        == "High"
                    ).sum()
                ),

            "immediate_maintenance_engines":
                int(
                    (
                        self.latest_df["Maintenance_Priority"]
                        == "Immediate"
                    ).sum()
                ),

            "average_rul":
                float(
                    round(
                        self.latest_df["Predicted_RUL"].mean(),
                        2
                    )
                )
        }
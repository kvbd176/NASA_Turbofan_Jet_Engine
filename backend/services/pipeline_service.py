# services/pipeline_service.py

from agents.health_monitoring_agent import HealthMonitoringAgent
from agents.rul_agent import RULAgent
from agents.maintenance_agent import (
    MaintenanceRecommendationAgent
)
import os


class PipelineService:

    def __init__(self):

        self.health_agent = HealthMonitoringAgent()

        self.rul_agent = RULAgent()

        self.maintenance_agent = (
            MaintenanceRecommendationAgent()
        )

    def run_pipeline(self, df):

        if "RUL" not in df.columns:

            max_cycle = (
                df.groupby("engine_id")["cycle"]
                .transform("max")
            )

            df["RUL"] = max_cycle - df["cycle"]

        df = self.health_agent.monitor(df)

        df = self.rul_agent.predict(df)

        df = self.maintenance_agent.recommend(df)

        return df

    def save_output(self,df,user_id):
        output_folder=(f"processed/user_{user_id}")

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        output_file = (
            f"{output_folder}/final_output.csv"
        )

        df.to_csv(
            output_file,
            index=False
        )

        return output_file
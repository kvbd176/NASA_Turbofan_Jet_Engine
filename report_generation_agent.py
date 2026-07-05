import pandas as pd

class ReportGenerationAgent:

    def generate(self, df):

        report = {
            "Total_Engines": df["engine_id"].nunique(),
            "Healthy": (df["Health_Status"] == "Healthy").sum(),
            "Degrading": (df["Health_Status"] == "Degrading").sum(),
            "Critical": (df["Health_Status"] == "Critical").sum(),
            "Faults_Detected": (df["Fault_Status"] == "Fault Detected").sum(),
            "High_Risk": (df["Risk_Level"] == "High").sum(),
            "Immediate_Maintenance":
                (df["Maintenance_Priority"] == "Immediate").sum(),
            "Average_RUL": round(df["Predicted_RUL"].mean(), 2)
        }

        report_df = pd.DataFrame(
            report.items(),
            columns=["Metric", "Value"]
        )

        report_df.to_csv(
            "system_report.csv",
            index=False
        )

        return report_df
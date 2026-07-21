import pandas as pd

class ReportGenerationAgent:

    def generate(self, df):

        # Latest record of each engine
        latest_df = (
            df.sort_values("cycle")
              .groupby("engine_id")
              .tail(1)
        )

        report = {

            # Engine statistics
            "Total_Engines": latest_df["engine_id"].nunique(),

            "Healthy_Engines":
                (latest_df["Health_Status"] == "Healthy").sum(),

            "Degrading_Engines":
                (latest_df["Health_Status"] == "Degrading").sum(),

            "Critical_Engines":
                (latest_df["Health_Status"] == "Critical").sum(),

            "Faulty_Engines":
                (latest_df["Fault_Status"] == "Fault Detected").sum(),

            "High_Risk_Engines":
                (latest_df["Risk_Level"] == "High").sum(),

            "Immediate_Maintenance_Engines":
                (latest_df["Maintenance_Priority"] == "Immediate").sum(),

            # Row statistics
            "Healthy_Rows":
                (df["Health_Status"] == "Healthy").sum(),

            "Degrading_Rows":
                (df["Health_Status"] == "Degrading").sum(),

            "Critical_Rows":
                (df["Health_Status"] == "Critical").sum(),

            "Average_RUL":
                round(latest_df["Predicted_RUL"].mean(), 2)

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

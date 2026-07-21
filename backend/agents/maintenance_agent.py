class MaintenanceRecommendationAgent:
    def recommend(self, df):
        df = df.copy()

        def priority(row):
            if (
                row["Risk_Level"] == "High"
                or row["Fault_Status"] == "Fault Detected"
                or row["Predicted_RUL"] <= 20
            ):
                return "Immediate"

            elif (
                row["Risk_Level"] == "Medium"
                or row["Predicted_RUL"] <= 50
                or row["Health_Status"] == "Degrading"
            ):
                return "Scheduled"

            else:
                return "Routine"

        df["Maintenance_Priority"] = df.apply(priority, axis=1)

        def recommendation(row):
            if row["Maintenance_Priority"] == "Immediate":
                return (
                    "Stop engine operation. Perform immediate inspection and "
                    "replace faulty components."
                )

            elif row["Maintenance_Priority"] == "Scheduled":
                return (
                    "Schedule preventive maintenance. Inspect engine during "
                    "the next maintenance cycle."
                )

            else:
                return (
                    "Engine operating normally. Continue routine monitoring "
                    "and follow the standard maintenance schedule."
                )

        df["Maintenance_Action"] = df.apply(recommendation, axis=1)

        return df
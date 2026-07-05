import re
import pandas as pd


class RAGAgent:

    def __init__(self,
                 data_file="final_output.csv",
                 report_file="system_report.csv"):

        self.data = pd.read_csv(data_file)
        self.report = pd.read_csv(report_file)

        # Ensure engine_id is numeric
        self.data["engine_id"] = pd.to_numeric(
            self.data["engine_id"], errors="coerce"
        ).astype("Int64")

    def retrieve(self, query):

        query = query.lower().strip()

        # -------------------------------
        # Immediate Maintenance
        # -------------------------------
        if "immediate" in query and "maintenance" in query:

            result = self.data[
                self.data["Maintenance_Priority"] == "Immediate"
            ]

            return result[
                [
                    "engine_id",
                    "Predicted_RUL",
                    "Risk_Level",
                    "Maintenance_Action"
                ]
            ]

        # -------------------------------
        # High Risk Engines
        # -------------------------------
        elif "high risk" in query:

            result = self.data[
                self.data["Risk_Level"] == "High"
            ]

            return result[
                [
                    "engine_id",
                    "Health_Status",
                    "Risk_Level",
                    "Predicted_RUL"
                ]
            ]

        # -------------------------------
        # Critical Engines
        # -------------------------------
        elif "critical" in query:

            result = self.data[
                self.data["Health_Status"] == "Critical"
            ]

            return result[
                [
                    "engine_id",
                    "Health_Status",
                    "Predicted_RUL"
                ]
            ]

        # -------------------------------
        # Engine List
        # -------------------------------
        elif (
            "which engines" in query
            or "engine list" in query
            or "engines are present" in query
            or "list of engines" in query
        ):

            engines = sorted(self.data["engine_id"].dropna().unique())

            return pd.DataFrame({"engine_id": engines})

        # -------------------------------
        # Specific Engine
        # -------------------------------
        elif "engine" in query:

            match = re.search(r"engine\s*(\d+)", query)

            if not match:
                return "Please specify a valid engine number."

            engine = int(match.group(1))

            result = self.data[self.data["engine_id"] == engine]

            if result.empty:
                return f"Engine {engine} not found."

            # Return latest cycle information
            if "cycle" in result.columns:
                result = result.sort_values("cycle").tail(1)

            return result[
                [
                    "engine_id",
                    "Health_Status",
                    "Predicted_RUL",
                    "Risk_Level",
                    "Maintenance_Action"
                ]
            ]

        # -------------------------------
        # Report Summary
        # -------------------------------
        elif "report" in query or "summary" in query:

            return self.report

        # -------------------------------
        # General Statistics
        # -------------------------------
        elif "statistics" in query or "overall" in query:

            return self.report

        # -------------------------------
        # Default
        # -------------------------------
        else:

            return (
                "No relevant information found.\n\n"
                "Try questions like:\n"
                "- What is the health status of engine 5?\n"
                "- Show high risk engines.\n"
                "- Which engines require immediate maintenance?\n"
                "- List critical engines.\n"
                "- Which engines are present?\n"
                "- Show report summary."
            )

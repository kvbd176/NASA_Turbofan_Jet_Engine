import pandas as pd


class RAGAgent:

    def __init__(self,
                 data_file="final_output.csv",
                 report_file="system_report.csv"):

        self.data = pd.read_csv(data_file)
        self.report = pd.read_csv(report_file)

    def retrieve(self, query):

        query = query.lower()

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
        # Specific Engine
        # -------------------------------
        elif "engine" in query:

            words = query.split()

            engine = None

            for word in words:

                if word.isdigit():
                    engine = int(word)
                    break

            if engine is not None:

                result = self.data[
                    self.data["engine_id"] == engine
                ]

                return result

            return "Engine number not found."

        # -------------------------------
        # Report Summary
        # -------------------------------
        elif "report" in query or "summary" in query:

            return self.report

        else:

            return "No relevant information found."
import re
import pandas as pd
class RAGAgent:
    def __init__(
        self,
        data_file="final_output.csv",
        report_file="system_report.csv"
    ):
        self.data = pd.read_csv(data_file)
        self.report = pd.read_csv(report_file)
        print("Data Loaded Successfully")
        print("Engine ID Type:", self.data["engine_id"].dtype)
    def retrieve(self, query):
        query = query.lower()
        # -------------------------------
        # Immediate Maintenance
        # -------------------------------
        if "immediate" in query and "maintenance" in query:
            result = self.data[self.data["Maintenance_Priority"] == "Immediate"]
            return result[["engine_id","Predicted_RUL","Risk_Level","Maintenance_Action"]]
        # -------------------------------
        # High Risk Engines
        # -------------------------------
        elif "high risk" in query:
            result = self.data[self.data["Risk_Level"] == "High"]
            return result[["engine_id","Health_Status","Risk_Level","Predicted_RUL"]]
        # -------------------------------
        # Critical Engines
        # -------------------------------
        elif "critical" in query:
            result = self.data[self.data["Health_Status"] == "Critical"]
            return result[["engine_id","Health_Status","Predicted_RUL"]]
        # -------------------------------
        # Specific Engine Query
        # -------------------------------
        elif "engine" in query:
            match = re.search(r"\d+", query)

            if not match:
                available = sorted(self.data["engine_id"].unique())
                return (
                    f"Please provide an engine number. "
                    f"Available engine IDs range from "
                    f"{available[0]} to {available[-1]}."
                )
            
            engine = int(match.group())
            
            result = self.data[self.data["engine_id"].astype(int) == engine]
            
            if result.empty:
                available = sorted(self.data["engine_id"].unique())
                return (
                    f"Engine {engine} not found. "
                    f"Available engine IDs range from "
                    f"{available[0]} to {available[-1]}."
                )
            latest = result.loc[result["cycle"].idxmax()]
            # Health Status
            if "health" in query:
                return (
                    f"Engine {engine} is currently "
                    f"{latest['Health_Status']} "
                    f"with a health score of "
                    f"{latest['Health_Score']:.2f}."
                )
            # RUL
            elif "rul" in query or "remaining useful life" in query:
                return (
                    f"Predicted RUL of Engine {engine} "
                    f"is {latest['Predicted_RUL']} cycles."
                )
            # Risk
            elif "risk" in query:
                return (
                    f"Engine {engine} is classified as "
                    f"{latest['Risk_Level']} Risk."
                )
            # Fault
            elif "fault" in query:
                return (
                    f"Fault Status of Engine {engine}: "
                    f"{latest['Fault_Status']}."
                )
            # Maintenance
            elif "maintenance" in query:
                return (
                    f"Recommended maintenance action for "
                    f"Engine {engine}: "
                    f"{latest['Maintenance_Action']}"
                )
            # Explanation
            elif "why" in query or "explain" in query:
                return latest["Explanation"]
            # Full Summary
            else:
                return pd.DataFrame(
                    {
                        "engine_id": [latest["engine_id"]],
                        "Health_Status": [latest["Health_Status"]],
                        "Risk_Level": [latest["Risk_Level"]],
                        "Predicted_RUL": [latest["Predicted_RUL"]],
                        "Fault_Status": [latest["Fault_Status"]],
                        "Maintenance_Action": [latest["Maintenance_Action"]]
                    }
                )
        # -------------------------------
        # Report Summary
        # -------------------------------
        elif "report" in query or "summary" in query:
            return self.report
        # -------------------------------
        # Unknown Query
        # -------------------------------
        else:
            return "No relevant information found."

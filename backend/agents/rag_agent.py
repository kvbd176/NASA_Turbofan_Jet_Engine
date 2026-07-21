import re

from agents.dashboard_agent import DashboardAgent
from agents.analytics_agent import AnalyticsAgent
from agents.report_generation_agent import ReportGenerationAgent


class RAGAgent:

    def __init__(self, user_id):

        self.user_id = user_id

        self.dashboard_agent = DashboardAgent(
            user_id
        )

        self.analytics_agent = AnalyticsAgent()

        self.report_agent = ReportGenerationAgent()

    

    def retrieve(self, query):

        query = query.lower()

        # -------------------------------
        # Dashboard KPIs
        # -------------------------------

        if (
            "dashboard" in query
            or "kpi" in query
            or "overview" in query
        ):
            return self.dashboard_agent.get_kpis()

        # -------------------------------
        # Health Distribution
        # -------------------------------

        elif "health distribution" in query:

            return self.analytics_agent.health_distribution(self.user_id)

        # -------------------------------
        # Risk Distribution
        # -------------------------------

        elif "risk distribution" in query:

            return self.analytics_agent.risk_distribution(self.user_id)

        # -------------------------------
        # Fault Distribution
        # -------------------------------

        elif "fault distribution" in query:

            return self.analytics_agent.fault_distribution(self.user_id)

        # -------------------------------
        # Maintenance Distribution
        # -------------------------------

        elif "maintenance distribution" in query:

            return self.analytics_agent.maintenance_distribution(self.user_id)

        # -------------------------------
        # Critical Engines
        # -------------------------------

        elif "critical engines" in query:

            return self.report_agent.critical_engines_report(self.user_id)

        # -------------------------------
        # Maintenance Report
        # -------------------------------

        elif "maintenance report" in query:

            return self.report_agent.maintenance_report(self.user_id)

        # -------------------------------
        # System Report
        # -------------------------------

        elif (
            "system report" in query
            or "report summary" in query
        ):

            return self.report_agent.generate_system_report(self.user_id)

        # -------------------------------
        # Engine Query
        # -------------------------------

        elif "engine" in query:

            match = re.search(r"\d+", query)

            if not match:

                return {
                    "error":
                    "Please provide an engine id."
                }

            engine_id = int(match.group())

            return self.report_agent.engine_report(self.user_id,engine_id)

        # -------------------------------
        # Unknown Query
        # -------------------------------

        return {
            "message":
            "No relevant information found."
        }
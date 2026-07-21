from fault_detection_agent import FaultDetectionAgent
from risk_analysis_agent import RiskAnalysisAgent
from explainability_agent import ExplainabilityAgent

class RULAgent:
    def __init__(self):
        self.fault_agent=FaultDetectionAgent()
        self.risk_agent=RiskAnalysisAgent()
        self.explain_agent=ExplainabilityAgent()

    def predict(self, df):
        # Step 1: Fault Detection
        fault_output=self.fault_agent.detect(df)
        # Step 2: Risk Analysis
        risk_output=self.risk_agent.analyze(fault_output)
        # Step 3: Explainability
        explain_output=self.explain_agent.explain(risk_output)
        # Step 4: RUL Prediction
        explain_output["Predicted_RUL"]=(explain_output["RUL"])
        return explain_output
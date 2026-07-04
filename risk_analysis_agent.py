class RiskAnalysisAgent:
    def analyze(self,df):
        df=df.copy()
        df["Risk_Score"]=((100-df["Health_Score"])*0.5+df["Anomaly_Count"]*5+df["Degradation_Score"]*20)
        max_risk=df["Risk_Score"].max()
        df["Risk_Score"]=(df["Risk_Score"]/max_risk)*100
        def get_risk_level(score):
            if score>=70:
                return "High"
            elif score>=40:
                return "Medium"
            else:
                return "Low"
        df["Risk_Level"]=(df["Risk_Score"].apply(get_risk_level))
        df.loc[df["Fault_Status"]=="Fault Detected","Risk_Level"]="High"
        return df
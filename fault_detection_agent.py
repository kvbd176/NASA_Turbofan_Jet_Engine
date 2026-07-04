class FaultDetectionAgent:
    def detect(self,df):
        df=df.copy()
        def detect_fault(row):
            if row["Health_Status"]=="Critical":
                return "Fault Detected"
            elif row["Anomaly_Count"]>=3:
                return "Fault Detected"
            elif row["Degradation_Score"]>0.4:
                return "Fault Detected"
            else:
                return "Normal"
        df["Fault_Status"]=(df.apply(detect_fault,axis=1))
        df["Fault_Alert"]=(
            df["Fault_Status"]
            .apply(
                lambda x:
                "Further analysis required"
                if x=="Fault Detected"
                else "No Alert"
            )
        )
        return df
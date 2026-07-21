import pandas as pd
import numpy as np


class HealthMonitoringAgent:
    def __init__(self,window_size=10):
        self.window_size=window_size
        
    def get_sensor_columns(self, df):
        sensor_cols=[
            col for col in df.columns
            if col.startswith("sensor")
        ]
        return sensor_cols

    def calculate_trends(self, df, sensor_cols):
        for sensor in sensor_cols:
            df[f"{sensor}_trend"]=(
                df.groupby("engine_id")[sensor].transform(
                    lambda x: x.rolling(
                        window=self.window_size,
                        min_periods=1
                    ).mean()
                )
            )
        return df

    def calculate_degradation_score(self, df, sensor_cols):
       baseline=(df.groupby("engine_id")[sensor_cols].transform("first"))
       df["Degradation_Score"]=(np.abs(df[sensor_cols]-baseline).mean(axis=1))
       return df

    def calculate_degradation_health(self, df):
        max_deg=max(df["Degradation_Score"].max(),1)
        df["Degradation_Health"]=(100-(df["Degradation_Score"]/max_deg)*100)
        df["Degradation_Health"]=(df["Degradation_Health"].clip(lower=0))
        return df

    def detect_anomalies(self,df,sensor_cols):
        for sensor in sensor_cols:
            std=df[sensor].std()
            if std==0:
                df[f"{sensor}_anomaly"]=0
            else:
                zscore=(df[sensor]-df[sensor].mean())/std
                df[f"{sensor}_anomaly"]=(np.abs(zscore)>3).astype(int)
        anomaly_cols=[
            col
            for col in df.columns
            if "_anomaly" in col
        ]
        df["Anomaly_Count"]=(df[anomaly_cols].sum(axis=1))
        return df

    def calculate_rul_health(self, df):
        max_rul=max(df["RUL"].max(),1)
        df["RUL_Health"]=(df["RUL"]/max_rul)*100
        df["RUL_Health"]=(df["RUL_Health"].clip(0, 100))
        return df

    def calculate_final_health_score(self, df):
        max_anomaly=max(df["Anomaly_Count"].max(),1)
        df["Anomaly_Health"]=(100-(df["Anomaly_Count"]/max_anomaly)*100)
        df["Health_Score"]=(0.4*df["Degradation_Health"]+0.4*df["RUL_Health"]+0.2*df["Anomaly_Health"])
        return df

    def assign_health_status(self,df):
        def status(score):
            if score>=70:
                return "Healthy"
            elif score>=40:
                return "Degrading"
            else:
                return "Critical"
        df["Health_Status"]=(df["Health_Score"].apply(status))
        return df

    def generate_alerts(self,df):
        def alert(row):
            if row["Health_Status"]=="Critical":
                return "Immediate inspection required"
            elif row["Health_Status"]=="Degrading":
                return "Monitor engine closely"
            return "Normal operation"
        df["Alert"]=df.apply(alert,axis=1)
        return df

    def monitor(self,df):
        sensor_cols=self.get_sensor_columns(df)
        df=self.calculate_trends(df,sensor_cols)
        df=self.calculate_degradation_score(df,sensor_cols)
        df=self.calculate_degradation_health(df)
        df=self.detect_anomalies(df,sensor_cols)
        df=self.calculate_rul_health(df)
        df=self.calculate_final_health_score(df)
        df=self.assign_health_status(df)
        df=self.generate_alerts(df)
        return df
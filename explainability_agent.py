class ExplainabilityAgent:
    def explain(self, df):
        df=df.copy()
        sensor_cols=[
            col
            for col in df.columns
            if col.startswith("sensor")
            and "_trend" not in col
            and "_anomaly" not in col
        ]
        baseline=(df.groupby("engine_id").first()[sensor_cols])
        key_factors=[]
        for _, row in df.iterrows():
            engine=row["engine_id"]
            base=baseline.loc[engine]
            current=row[sensor_cols]
            deviation=abs(current-base)
            key_sensor=deviation.idxmax()
            key_factors.append(key_sensor)
        df["Key_Factor"]=key_factors
        def generate_explanation(row):
            return (
                f"Engine classified as "
                f"{row['Health_Status']} "
                f"with {row['Risk_Level']} risk. "
                f"Primary degradation observed in "
                f"{row['Key_Factor']}."
            )
        df["Explanation"]=(df.apply(generate_explanation,axis=1))
        return df
from data_preprocessingagent import DataPreprocessingAgent
from health_monitoring_agent import HealthMonitoringAgent


def main():

    print("=" * 50)
    print("NASA Turbofan Predictive Maintenance System")
    print("=" * 50)

    # -------------------------
    # Agent 1 : Data Preprocessing
    # -------------------------

    print("\n[1] Running Data Preprocessing Agent...")

    preprocessing_agent=DataPreprocessingAgent()
    train,test,rul=preprocessing_agent.preprocess(
        "train_FD003.txt",
        "test_FD003.txt",
        "RUL_FD003.txt"
    )
    print("Data Preprocessing Completed")
    # -------------------------
    # Agent 2 : Health Monitoring
    # -------------------------

    print("\n[2] Running Health Monitoring Agent...")
    health_agent=HealthMonitoringAgent()
    health_output=health_agent.monitor(train)
    print("Health Monitoring Completed")

    # -------------------------
    # Save Results
    # -------------------------

    health_output.to_csv(
        "health_monitoring_output.csv",
        index=False
    )

    print("\nOutput Saved:")
    print("health_monitoring_output.csv")

    # -------------------------
    # Sample Results
    # -------------------------

    print("\nSample Results:\n")
    print(
        health_output[
            [
                "engine_id",
                "cycle",
                "RUL",
                "Health_Score",
                "Health_Status",
                "Alert"
            ]
        ].head(10)
    )
    print("\nPipeline Completed Successfully")

if __name__ == "__main__":
    main()
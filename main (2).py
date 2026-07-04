from data_preprocessingagent import DataPreprocessingAgent
from health_monitoring_agent import HealthMonitoringAgent
from rul_agent import RULAgent


def main():

    print("=" * 50)
    print("NASA Turbofan Predictive Maintenance System")
    print("=" * 50)

    # -------------------------
    # Agent 1 : Data Preprocessing
    # -------------------------

    print("\n[1] Running Data Preprocessing Agent...")

    preprocessing_agent = DataPreprocessingAgent()

    train, test, rul = preprocessing_agent.preprocess(
        "train_FD003.txt",
        "test_FD003.txt",
        "RUL_FD003.txt"
    )

    print("Data Preprocessing Completed")

    # -------------------------
    # Agent 2 : Health Monitoring
    # -------------------------

    print("\n[2] Running Health Monitoring Agent...")

    health_agent = HealthMonitoringAgent()

    health_output = health_agent.monitor(train)

    print("Health Monitoring Completed")

    # -------------------------
    # Agent 3 : RUL Agent
    # -------------------------

    print("\n[3] Running RUL Agent...")

    rul_agent = RULAgent()

    rul_output = rul_agent.predict(
        health_output
    )

    print("RUL Agent Completed")

    # -------------------------
    # Save Results
    # -------------------------

    rul_output.to_csv(
        "rul_agent_output.csv",
        index=False
    )

    print("\nOutput Saved:")
    print("rul_agent_output.csv")

    # -------------------------
    # Sample Results
    # -------------------------

    print("\nSample Results:\n")

    print(
        rul_output[
            [
                "engine_id",
                "cycle",
                "Predicted_RUL",
                "Fault_Status",
                "Risk_Level",
                "Key_Factor"
            ]
        ].head(10)
    )

    print(
        rul_output[
            [
                "engine_id",
                "Health_Status",
                "Risk_Level",
                "Key_Factor",
                "Explanation"
            ]
        ].head(10)
    )

    print("\nPipeline Completed Successfully")


if __name__ == "__main__":
    main()
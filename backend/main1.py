from data_preprocessingagent import DataPreprocessingAgent
from health_monitoring_agent import HealthMonitoringAgent
from rul_agent import RULAgent
from maintenance_agent import MaintenanceRecommendationAgent
from report_generation_agent import ReportGenerationAgent
from rag_agent import RAGAgent

def main():
    print("=" * 50)
    print("NASA Turbofan Predictive Maintenance System")
    print("=" * 50)
    # -------------------------
    # Agent 1 : Data Preprocessing
    # -------------------------
    print("\n[1] Running Data Preprocessing Agent...")
    preprocessing_agent=DataPreprocessingAgent()
    train, test, rul=preprocessing_agent.preprocess(
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
    # Agent 3 : RUL Agent
    # -------------------------
    print("\n[3] Running RUL Agent...")
    rul_agent=RULAgent()
    rul_output=rul_agent.predict(health_output)
    print("RUL Agent Completed")
    # -------------------------
    # Agent 4 : Maintenance Agent
    # -------------------------
    print("\n[4] Running Maintenance Recommendation Agent...")
    maintenance_agent=MaintenanceRecommendationAgent()
    final_output=maintenance_agent.recommend(rul_output)
    print("Maintenance Recommendation Completed")
    # -------------------------
    # Report Generation Agent
    # -------------------------
    print("\n[5] Running Report Generation Agent...")
    report_agent=ReportGenerationAgent()
    report=report_agent.generate(final_output)
    print("Report Generation Completed")
    print("\nSystem Report:\n")
    print(report)
    # -------------------------
    # Save Results
    # -------------------------
    final_output.to_csv(
        "final_output.csv",
        index=False
    )
    print("\nOutput Saved:")
    print("final_output.csv")
    # -------------------------
    # Sample Results
    # -------------------------
    print("\nSample Results:\n")
    print(
        final_output[
            [
                "engine_id",
                "cycle",
                "Predicted_RUL",
                "Health_Status",
                "Fault_Status",
                "Risk_Level",
                "Maintenance_Priority",
                "Maintenance_Action"
            ]
        ].head(10)
    )
    print(final_output[["engine_id","Key_Factor","Explanation","Maintenance_Action"]].head(10))
    print("\nPipeline Completed Successfully")
    # -------------------------
    # Agent 6 : RAG Agent
    # -------------------------
    print("\n[6] Running RAG Agent...")
    rag_agent=RAGAgent(
        data_file="final_output.csv",
        report_file="system_report.csv"
    )
    print("RAG Agent Ready!")
    print("\nYou can now ask questions about the engine data.")
    print("Type 'exit' to quit.\n")
    while True:
        query=input("Question: ")
        if query.lower()=="exit":
            print("Exiting chatbot...")
            break
        result=rag_agent.retrieve(query)
        print("\nRetrieved Information:\n")
        print(result)
if __name__ == "__main__":
    main()
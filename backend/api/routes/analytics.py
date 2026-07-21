from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user
from agents.analytics_agent import AnalyticsAgent

router = APIRouter()

analytics_agent = AnalyticsAgent()


def no_dataset_response():
    return {
        "status": "NO_DATA",
        "message": "Dataset not uploaded or processed yet. Please upload a dataset and run the pipeline."
    }


@router.get("/health-distribution")
def health_distribution(
    current_user=Depends(get_current_user)
):
    try:
        return analytics_agent.health_distribution(
            current_user.id
        )
    except Exception:
        return no_dataset_response()


@router.get("/risk-distribution")
def risk_distribution(
    current_user=Depends(get_current_user)
):
    try:
        return analytics_agent.risk_distribution(
            current_user.id
        )
    except Exception:
        return no_dataset_response()


@router.get("/fault-distribution")
def fault_distribution(
    current_user=Depends(get_current_user)
):
    try:
        return analytics_agent.fault_distribution(
            current_user.id
        )
    except Exception:
        return no_dataset_response()


@router.get("/maintenance-distribution")
def maintenance_distribution(
    current_user=Depends(get_current_user)
):
    try:
        return analytics_agent.maintenance_distribution(
            current_user.id
        )
    except Exception:
        return no_dataset_response()


@router.get("/critical-engines")
def critical_engines(
    current_user=Depends(get_current_user)
):
    try:
        return analytics_agent.critical_engines(
            current_user.id
        )
    except Exception:
        return no_dataset_response()


@router.get("/rul-distribution")
def rul_distribution(
    current_user=Depends(get_current_user)
):
    try:
        return analytics_agent.rul_distribution(
            current_user.id
        )
    except Exception:
        return no_dataset_response()
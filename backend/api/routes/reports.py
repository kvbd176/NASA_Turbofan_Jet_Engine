from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user
from agents.report_generation_agent import ReportGenerationAgent


router = APIRouter()


report_agent = ReportGenerationAgent()


def no_dataset_response():
    return {
        "status": "NO_DATA",
        "message": "Dataset not uploaded or processed yet.",
        "action": "Upload dataset and run pipeline."
    }


@router.get("/system")
def system_report(
    current_user=Depends(get_current_user)
):

    try:

        return report_agent.generate_system_report(
            current_user.id
        )

    except Exception:

        return no_dataset_response()



@router.get("/critical-engines")
def critical_engines_report(
    current_user=Depends(get_current_user)
):

    try:

        return report_agent.critical_engines_report(
            current_user.id
        )

    except Exception:

        return no_dataset_response()



@router.get("/maintenance")
def maintenance_report(
    current_user=Depends(get_current_user)
):

    try:

        return report_agent.maintenance_report(
            current_user.id
        )

    except Exception:

        return no_dataset_response()



@router.get("/engine/{engine_id}")
def engine_report(
    engine_id: int,
    current_user=Depends(get_current_user)
):

    try:

        return report_agent.engine_report(
            current_user.id,
            engine_id
        )

    except Exception:

        return no_dataset_response()
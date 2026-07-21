from fastapi import APIRouter, Depends

from agents.dashboard_agent import DashboardAgent
from auth.dependencies import get_current_user


router = APIRouter()


def no_dataset_response():
    return {
        "status": "NO_DATA",
        "message": "Dataset not uploaded or processed yet.",
        "action": "Upload dataset and run pipeline."
    }


@router.get("/kpis")
def get_kpis(
    current_user=Depends(get_current_user)
):

    try:

        dashboard_agent = DashboardAgent(
            current_user.id
        )

        return dashboard_agent.get_kpis()


    except Exception as e:

        if str(e) == "No processed dataset found":
            return no_dataset_response()

        raise e
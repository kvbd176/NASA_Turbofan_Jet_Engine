from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from auth.dependencies import get_current_user

from services.data_service import (
    get_user_dataset_path,
    process_user_dataset
)


router = APIRouter()


@router.post("/run")
def run_pipeline(
    current_user=Depends(get_current_user)
):

    dataset = get_user_dataset_path(
        current_user.id
    )


    if dataset is None:

        raise HTTPException(
            status_code=404,
            detail={
                "status": "NO_DATASET",
                "message": "Upload dataset first"
            }
        )


    try:

        result = process_user_dataset(
            current_user.id
        )


        return {
            "status": "SUCCESS",
            "user_id": current_user.id,
            "result": result
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail={
                "status": "PIPELINE_FAILED",
                "message": str(e)
            }
        )
from fastapi import APIRouter

router = APIRouter()

@router.get("/check-v1-health")
async def read_data():
    return {"message": "Success from v1!"}
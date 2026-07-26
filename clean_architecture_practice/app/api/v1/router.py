from fastapi import APIRouter
from app.api.v1.endpoints import measurements

router = APIRouter()

router.post("/measurements")(measurements.add_measurement)
router.get("/measurements/{user_id}")(measurements.get_history)
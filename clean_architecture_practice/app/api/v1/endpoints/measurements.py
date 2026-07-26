from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.services.measurement_service import MeasurementService
from app.schemas.measurement import MeasurementCreate, MeasurementResponse

async def add_measurement(
    data: MeasurementCreate,
    session: AsyncSession = Depends(get_session)
):
    service = MeasurementService(session)
    measurement = await service.create_measurement(data)
    return MeasurementResponse.model_validate(measurement)

async def get_history(
    user_id: int,
    limit: int = 5,
    session: AsyncSession = Depends(get_session)
):
    service = MeasurementService(session)
    history = await service.get_history(user_id, limit)
    return [MeasurementResponse.model_validate(m) for m in history]
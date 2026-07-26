from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.measurement import Measurement
from app.schemas.measurement import MeasurementCreate

class MeasurementService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_measurement(self, data: MeasurementCreate) -> Measurement:
        imt = round(data.weight / (data.height ** 2), 1)
        measurement = Measurement(
            user_id=data.user_id,
            weight=data.weight,
            height=data.height,
            imt=imt
        )
        self.session.add(measurement)
        await self.session.commit()
        await self.session.refresh(measurement)
        return measurement

    async def get_history(self, user_id: int, limit: int = 5):
        result = await self.session.execute(
            select(Measurement)
            .where(Measurement.user_id == user_id)
            .order_by(Measurement.created_at.desc())
            .limit(limit)
        )
        return result.scalars().all()
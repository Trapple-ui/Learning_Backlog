from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from database import SessionFactory, Resources
from schemas import ResourcesGet

router = APIRouter(prefix='/resources', tags=['Resources'])

@router.get('/')
def get_all_resources() -> List[ResourcesGet]:
    with SessionFactory() as session:
        query = select(Resources)
        result = session.execute(query)
        res_models = result.scalars().all()
        res_schemas = [ResourcesGet.model_validate(res_model) for res_model in res_models]

        return res_schemas
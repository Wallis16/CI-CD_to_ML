import requests

from fastapi import APIRouter
from pydantic import BaseModel
from app.models import *

class Parameters(BaseModel):
    learning_rate: float
    epochs: int
    loss: str
    optimizer: str | None = None

router = APIRouter()

@router.post('/model/{model_name}', tags=['Training'])
async def model_training(model_name: str, parameters: Parameters | None = None):

    model = {'model': model_name}

    if parameters:
        model.update({'parameters': parameters})


    if requests.get('&'+model_name):
        model_name.train()


    return model

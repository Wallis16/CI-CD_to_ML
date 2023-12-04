from fastapi import APIRouter
from pydantic import BaseModel

class Parameters(BaseModel):
    learning_rate: float
    epochs: int
    loss: str
    optimizer: str | None = None

router = APIRouter()

@router.post('/model/{model_name}', tags=['Inference'])
async def model_inference(model_name: str, parameters: Parameters | None = None):
    model = {'model': model_name}

    if parameters:
        model.update({'parameters': parameters})

    return model

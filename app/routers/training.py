from fastapi import APIRouter
from pydantic import BaseModel
from models import keras1, keras2

class Parameters(BaseModel):
    learning_rate: float | None = None
    epochs: int
    loss: str | None = None
    optimizer: str | None = None

router = APIRouter()

@router.post('/model/{model_name}', tags=['Training'])
async def model_training(model_name: str, data_path: str, parameters: Parameters | None = None):

    model = {'model': model_name}

    if parameters:
        model.update({'parameters': parameters})

    if model_name == 'keras1':
        keras1.model_training(data_path=data_path,epochs=model['parameters'].epochs)
    if model_name == 'keras2':
        keras2.model_training(data_path=data_path,epochs=model['parameters'].epochs)

    return model

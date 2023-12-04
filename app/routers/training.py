from fastapi import APIRouter

router = APIRouter()

@router.get('/model_training/{model_name}', tags=['Training'])
async def model_inference(model_name: str):
    return {'model': model_name}

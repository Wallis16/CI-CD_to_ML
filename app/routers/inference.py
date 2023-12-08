from fastapi import APIRouter

router = APIRouter()

@router.get('/model_inference/{model_name}', tags=['Inference'])
async def model_inference(model_name: str):
    return {'model': model_name}

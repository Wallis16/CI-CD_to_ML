from fastapi import Depends, FastAPI
from dependencies import get_query_token, get_token_header
from routers import inference, training
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

origins = [
    'http://localhost.tiangolo.com',
    'https://localhost.tiangolo.com',
    'http://localhost',
    'http://localhost:8080',
]

app = FastAPI(title='Machine Learning', dependencies=[Depends(get_query_token)])

app.include_router(inference.router,dependencies=[Depends(get_token_header)])
app.include_router(training.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {'message': 'Hello Bigger Applications!'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

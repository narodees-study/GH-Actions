import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return {'status': 'ok'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)

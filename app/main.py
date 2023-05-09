import os

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return {'debug': int(os.getenv('DEBUG'))}

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return {'message': 'Hello World'}


if __name__ == '__main__':
    uvicorn.run(app, port=8055)

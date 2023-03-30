import uvicorn
from fastapi import FastAPI

from config import get_settings

settings = get_settings()


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=str(settings.APP_VERSION),
    docs_url=settings.DOCS_URL
)


@app.get('/')
async def main():
    return {'message': 'Hello World'}


if __name__ == '__main__':
    uvicorn.run(app, port=8055)

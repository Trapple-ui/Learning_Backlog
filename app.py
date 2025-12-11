from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    # await delete_tables()
    print('База очищена!')

    # await create_tables()
    print('База готова к работе')

    yield

app = FastAPI(title='Пет проект Учебный трекер', lifespan=lifespan, docs_url='/docs')

# проверка работоспособности
@app.get('/health', summary='Проверка работы')
def health_status():
    return {'status': 'ok'}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, access_log=False)
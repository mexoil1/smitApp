from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from insurance.router import router as insuranceRouter
from config import PG_DB, PG_HOST, PG_USERNAME, PG_PASSWORD

app = FastAPI(title="Расчет страховки")


app.include_router(insuranceRouter)


register_tortoise(
    app,
    db_url=f"asyncpg://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:5431/{PG_DB}",
    modules={"models": ["insurance.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

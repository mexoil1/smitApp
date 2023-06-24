from config import PG_DB, PG_HOST, PG_USERNAME, PG_PASSWORD

TORTOISE_ORM = {
    "connections": {"default": f"asyncpg://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:5431/{PG_DB}"},
    "apps": {
        "insurance": {
            "models": ["insurance.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
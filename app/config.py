from dotenv import load_dotenv
import os

load_dotenv()

PG_USERNAME=os.environ.get('PG_USERNAME')
PG_PASSWORD=os.environ.get('PG_PASSWORD')
PG_HOST=os.environ.get('PG_HOST')
PG_DB = os.environ.get('PG_DB')


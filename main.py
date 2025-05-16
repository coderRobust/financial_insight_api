from dotenv import load_dotenv
from app.api.routes import router
from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


load_dotenv()

app = FastAPI(title="Financial Insight Engine")
app.include_router(router)

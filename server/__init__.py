from fastapi import FastAPI
app = FastAPI()
from server.routes import stockRoutes
from server.routes import listRoutes
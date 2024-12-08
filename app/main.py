from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.router import auth, dashboard, player_stats

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes = [auth, dashboard, player_stats]

for route in routes:
    app.include_router(route.router)

@app.get("/")
async def index():
    return {
        "version": 0.1
    }
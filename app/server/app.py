from fastapi import FastAPI
from server.models.item_reward import ItemReward

from server.routes.item_reward import router as ItemRewardRouter

app = FastAPI()

app.include_router(ItemRewardRouter, tags=["item-reward"], prefix="/item-reward")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


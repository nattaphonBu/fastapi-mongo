from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_run_reward,
    add_item_reward,
    get_item_reward,
    # get_item_rewards
)
from server.models.item_reward import (
    ErrorResponseModel,
    ResponseModel,
    ItemReward,
)

router = APIRouter()

@router.post("/", response_description="Item Reward data added into the database")
async def add_item_reward_data(item: ItemReward = Body(...)):
    item = jsonable_encoder(item)
    new_item_reward = await add_item_reward(item)
    return ResponseModel(new_item_reward, "Item Reward added successfully.")

@router.get("/item-reward/id", response_description="Get Item Reward data from the database")
async def get_item_reward_datas(id):
    new_item_reward = await get_item_reward(id)
    return ResponseModel(new_item_reward, "Item Reward added successfully.")

@router.get("/item-rewards", response_description="Get Item Reward data from the database")
async def get_item_reward_data():
    new_item_reward = await retrieve_run_reward()
    return ResponseModel(new_item_reward, "Item Reward added successfully.")
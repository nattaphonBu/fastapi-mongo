import motor.motor_asyncio
from bson.objectid import ObjectId
MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.run_reward

run_reward_collection = database.get_collection("run_reward_collection")


def run_reward_helper(run_reward) -> dict:
    return {
        "id": str(run_reward["_id"]),
        "name": run_reward["name"],
        "amount": run_reward["amount"],
        "rate": run_reward["rate"],
    }

async def retrieve_run_reward():
    rewards = []
    async for reward in run_reward_collection.find():
        rewards.append(run_reward_helper(reward))
    return rewards

async def add_item_reward(item_reward_data: dict) -> dict:
    item = await run_reward_collection.insert_one(item_reward_data)
    new_item = await run_reward_collection.find_one({"_id": item.inserted_id})
    return run_reward_helper(new_item)

async def get_item_reward(item_id: int) -> dict:
    item = await run_reward_collection.find_one({"_id": ObjectId(item_id)})
    return run_reward_helper(item)


async def delete_item(item_id: int):
    item = await run_reward_collection.find_one({"_id": ObjectId(item_id)})
    if item:
        await run_reward_collection.delete_one({"_id": ObjectId(item_id)})
        return True
from typing import Optional

from pydantic import BaseModel, EmailStr, Field
class ItemReward(BaseModel):
    name: str = Field(...)
    amount: int = Field(...)
    rate: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Cheetos",
                "amount": 50,
                "rate": 2,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
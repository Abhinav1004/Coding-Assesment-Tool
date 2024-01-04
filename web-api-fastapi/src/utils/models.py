from pydantic import BaseModel, Field
from typing import List


class RequestModelGeneric(BaseModel):
    # TODO: Incomplete request model
    vector1: List = Field(
       title="vector1"
    )


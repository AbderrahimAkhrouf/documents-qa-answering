from pydantic import BaseModel, Field, validator, ConfigDict


class answer(BaseModel):
    response : str
    sources : str
    time : float | None
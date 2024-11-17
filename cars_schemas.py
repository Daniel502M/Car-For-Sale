from pydantic import BaseModel


class CarsCreateSchema(BaseModel):
    name: str
    duration: int
    price: float
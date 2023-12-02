from pydantic import BaseModel


class ExempleResponseSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class ExempleSchemaCreate(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True

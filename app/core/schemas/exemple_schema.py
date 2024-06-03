from pydantic import BaseModel, ConfigDict


class ExempleSchema(BaseModel):
    id: int
    name: str
    email: str


class ExempleSchemaCreate(BaseModel):
    name: str
    email: str
    model_config = ConfigDict(extra="forbid")


class ExempleSchemaUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    model_config = ConfigDict(extra="forbid")

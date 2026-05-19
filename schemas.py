from pydantic import BaseModel

class ItemBase(BaseModel):
    nome: str
    quantidade: int
    descricao: str

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True
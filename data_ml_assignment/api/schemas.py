from pydantic import BaseModel

class Resume(BaseModel):
    text: str

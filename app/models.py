from typing import Optional

from sqlmodel import SQLModel, Field

class Simple(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    string: str = Field(default="")
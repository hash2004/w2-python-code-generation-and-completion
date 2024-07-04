from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectResponse(ProjectCreate):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class TicketCreate(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default='open')
    priority: Optional[str] = Field(default='medium')


class TicketResponse(TicketCreate):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

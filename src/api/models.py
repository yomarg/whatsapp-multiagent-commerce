from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class Message(BaseModel):
    from_: str = Field(alias="from")
    id: str
    text: Optional[Dict[str, str]] = None
    type: str

class Value(BaseModel):
    messaging_product: str
    metadata: Dict[str, str]
    contacts: Optional[List[Dict[str, Any]]] = None
    messages: Optional[List[Message]] = None

class Change(BaseModel):
    value: Value
    field: str

class Entry(BaseModel):
    id: str
    changes: List[Change]

class WhatsAppWebhookSchema(BaseModel):
    object: str
    entry: List[Entry]

class SessionState(BaseModel):
    sender_id: str
    rubro_activo: Optional[str] = None
    history: List[Dict[str, str]] = Field(default_factory=list)

class RouterOutputSchema(BaseModel):
    rubro_asignado: str
    intencion_resumida: str
    urgencia: str

class HealthResponseSchema(BaseModel):
    status: str
    timestamp: datetime
    dependencies: Dict[str, str]

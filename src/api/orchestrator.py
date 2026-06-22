import json
import os
import asyncio
from src.api.models import WhatsAppWebhookSchema, RouterOutputSchema

async def process_whatsapp_message(payload: WhatsAppWebhookSchema):
    if not payload.entry or not payload.entry[0].changes:
        return
        
    value = payload.entry[0].changes[0].value
    if not value.messages:
        return
        
    message = value.messages[0]
    sender_id = message.from_
    
    if message.type == "text" and message.text:
        text_body = message.text["body"]
        
        # Triaje Dummy: En producción usaría Gemini Flash
        # y parsearía el JSON para extraer RouterOutputSchema.
        await asyncio.sleep(0.1)

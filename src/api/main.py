import os
from datetime import datetime
from fastapi import FastAPI, Query, HTTPException, BackgroundTasks
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from src.api.models import WhatsAppWebhookSchema, HealthResponseSchema
from src.api.orchestrator import process_whatsapp_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/webhook/whatsapp")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
):
    verify_token = os.getenv("WHATSAPP_VERIFY_TOKEN")
    
    if hub_mode == "subscribe" and hub_verify_token == verify_token:
        return PlainTextResponse(hub_challenge)
    raise HTTPException(status_code=403, detail="Verification failed")

@app.post("/webhook/whatsapp")
async def receive_webhook(
    payload: WhatsAppWebhookSchema,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(process_whatsapp_message, payload)
    return {"status": "ok"}

@app.get("/api/health", response_model=HealthResponseSchema)
async def health_check():
    return HealthResponseSchema(
        status="ok",
        timestamp=datetime.utcnow(),
        dependencies={"sqlite": "ok"}
    )

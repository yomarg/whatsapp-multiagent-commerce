# 📱 SKILL: META WHATSAPP CLOUD API REFERENCE
Esta skill rige la integración del backend (FastAPI) con la API Oficial de WhatsApp Cloud (Meta), garantizando un despliegue seguro y resiliente a baneos [cite: 392].

#### 🔗 FUENTE DE VERDAD
*   **Documentación Oficial**: https://developers.facebook.com/docs/whatsapp/cloud-api

#### ⚡ PATRONES ESTRUCTURALES (WEBHOOKS)
Cuando el Esquema 3 (Backend) programe la conexión, debe seguir estrictamente estos protocolos:
1.  **Validación del Webhook (GET)**: El endpoint `/webhook/whatsapp` debe aceptar peticiones GET. Debe extraer `hub.mode`, `hub.verify_token` y `hub.challenge`, y retornar únicamente el `hub.challenge` en texto plano (como entero) si el token coincide [cite: 428].
2.  **Recepción de Mensajes (POST)**: El mismo endpoint debe aceptar POST. Usar validación fuerte con Pydantic para el payload anidado (`entry.changes.value.messages`). Retornar un `HTTP 200 OK` inmediatamente antes de procesar la respuesta con la IA para evitar que Meta reenvíe el mensaje [cite: 388].
3.  **Envío de Mensajes (POST a Meta)**: Para responder al usuario, ejecutar peticiones HTTP utilizando el método `httpx.AsyncClient` apuntando a `https://graph.facebook.com/v19.0/{phone_number_id}/messages`.

#### 🛡️ SEGURIDAD Y GOBERNANZA (G-ZERO)
*   **Cero Hardcoding**: Los valores `WHATSAPP_TOKEN`, `WHATSAPP_VERIFY_TOKEN` y `WHATSAPP_PHONE_NUMBER_ID` DEBEN extraerse de `os.getenv()`. Prohibido quemar tokens en el código fuente.
*   **Asincronía**: Toda llamada HTTP a la API de Meta debe ser no bloqueante (`async/await`) para no saturar el servidor [cite: 303].
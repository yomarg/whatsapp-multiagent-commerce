# 🗄️ SKILL: RAG & DATABASE TOOL CALLING
Esta skill rige la interacción de los agentes especialistas comerciales con el motor de base de datos (ERP/PostgreSQL) mediante Tool Calling y la inyección de contexto RAG[cite: 382, 389].

#### 🛡️ PROTOCOLO DE GROUNDING FINANCIERO (INNEGOCIABLE)
* **Verdad Absoluta:** La IA tiene ESTRICTAMENTE PROHIBIDO inventar, asumir o calcular precios, aplicar descuentos no autorizados o confirmar niveles de stock[cite: 383].
* **Cero Alucinación:** La única fuente de verdad aceptable para emitir un mensaje comercial es el objeto JSON en crudo devuelto por la invocación a la herramienta de la base de datos[cite: 376, 383].

#### 🛠️ PATRONES DE INVOCACIÓN (TOOL CALLING)
Para interactuar con el inventario, el agente debe pausar su razonamiento (ReAct) e invocar de forma autónoma las herramientas expuestas en FastAPI:
1. `search_products(keyword)`: Para obtener listados de SKUs y descripciones validadas[cite: 392].
2. `check_stock(product_id, location)`: Para verificar existencia física en tiempo real antes de sugerir una compra al usuario[cite: 392].
3. `create_sale_order(partner_id, order_lines)`: Para generar presupuestos en estado borrador de manera transaccional[cite: 392].

#### ⚙️ ESTÁNDARES DE DESARROLLO BACKEND (DB CONNECTION)
Cuando el Especialista Backend programe o modifique estas herramientas, aplicará:
* **ORM Asíncrono:** Uso exclusivo de SQLAlchemy 2.0 (o drivers asíncronos equivalentes) para no bloquear el Event Loop de FastAPI[cite: 289, 304].
* **Validación Fuerte:** Mapeo estricto de entradas y salidas de la BD utilizando Pydantic v2[cite: 289].
* **Seguridad Anti-Inyección:** Prohibida la concatenación de variables (ej. f-strings) en consultas SQL. Todo acceso debe estar estrictamente parametrizado[cite: 366].
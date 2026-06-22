# Changelog
Todos los cambios notables en el sistema OmniCommerce AI Gateway serán documentados en este archivo.
El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/), y este proyecto adhiere al [Versionamiento Semántico](https://semver.org/lang/es/).

## [1.0.1] - 2026-06-21
### Añadido
- Refinamiento de la arquitectura asíncrona (Clean Architecture) para el gateway de WhatsApp.
- Micro-módulo de Health Check implementado en Backend y Frontend.
- Certificación empírica QA automatizada mediante pytest sobre endpoints base.

## [1.0.0-alpha] - 2026-06-21
### Añadido
- Inicialización de la arquitectura base del proyecto.
- Andamiaje del servidor asíncrono con FastAPI (`src/api/main.py`).
- Modelado de validación estricta con Pydantic v2 (`src/api/models.py`).
- Orquestador cognitivo base (`src/api/orchestrator.py`) y conectividad asíncrona SQLite (`src/tools/inventory.py`).
- Generación de Blueprints Técnicos (P1) y desgloses de ejecución (P2) para el micro-módulo de validación de estado (Health Check).

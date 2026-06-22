@echo off
echo ==============================================
echo Iniciando OmniCommerce AI Gateway (WhatsApp)
echo ==============================================

echo Comprobando entorno...

:: Iniciar el backend con uvicorn en una nueva ventana
echo [1] Iniciando Servidor Backend FastAPI en el puerto 8950...
start "OmniCommerce FastAPI" cmd /k "uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8950"

echo.
echo ==============================================
echo [INFO] Servidor backend levantado.
echo [INFO] El frontend de React se encuentra en 'frontend/'. (Asegurese de instalar dependencias y ejecutar 'npm run dev' en esa ruta).
echo ==============================================
echo.
echo Presione cualquier tecla para cerrar este launcher (los servidores seguiran corriendo en sus ventanas)...
pause > nul

@echo off
echo ==========================================
echo   Instalacion Dashboard Shopping Trends
echo ==========================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python no esta instalado
    echo Por favor instala Python 3.8 o superior
    pause
    exit /b 1
)

echo Python encontrado
python --version
echo.

REM Crear entorno virtual
echo Creando entorno virtual...
python -m venv venv

if errorlevel 1 (
    echo Error al crear entorno virtual
    pause
    exit /b 1
)

echo Entorno virtual creado
echo.

REM Activar entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo Error al activar entorno virtual
    pause
    exit /b 1
)

echo Entorno virtual activado
echo.

REM Instalar dependencias
echo Instalando dependencias (Django, Pandas)...
python -m pip install --upgrade pip
pip install django pandas

if errorlevel 1 (
    echo Error al instalar dependencias
    pause
    exit /b 1
)

echo Dependencias instaladas
echo.

REM Ejecutar migraciones
echo Ejecutando migraciones de base de datos...
python manage.py migrate

if errorlevel 1 (
    echo Error al ejecutar migraciones
    pause
    exit /b 1
)

echo Migraciones completadas
echo.

REM Verificar que shopping_trends.csv existe
if not exist "shopping_trends.csv" (
    echo Advertencia: No se encontro shopping_trends.csv
    echo Asegurate de tener el archivo CSV en el directorio proyecto/
    echo.
)

echo ==========================================
echo   Instalacion completada con exito
echo ==========================================
echo.
echo Para iniciar el servidor:
echo   1. Activa el entorno virtual (si no esta activado):
echo      venv\Scripts\activate
echo.
echo   2. Ejecuta el servidor:
echo      python manage.py runserver
echo.
echo   3. Abre tu navegador en:
echo      http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/
echo.
echo Para desactivar el entorno virtual:
echo      deactivate
echo.
pause

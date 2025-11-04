#!/bin/bash

echo "=========================================="
echo "  Instalación Dashboard Shopping Trends"
echo "=========================================="
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

echo "✓ Python encontrado: $(python3 --version)"
echo ""

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Error al crear entorno virtual"
    exit 1
fi

echo "✓ Entorno virtual creado"
echo ""

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Error al activar entorno virtual"
    exit 1
fi

echo "✓ Entorno virtual activado"
echo ""

# Instalar dependencias
echo "📥 Instalando dependencias (Django, Pandas)..."
pip install --upgrade pip
pip install django pandas

if [ $? -ne 0 ]; then
    echo "❌ Error al instalar dependencias"
    exit 1
fi

echo "✓ Dependencias instaladas"
echo ""

# Ejecutar migraciones
echo "🗄️  Ejecutando migraciones de base de datos..."
python manage.py migrate

if [ $? -ne 0 ]; then
    echo "❌ Error al ejecutar migraciones"
    exit 1
fi

echo "✓ Migraciones completadas"
echo ""

# Verificar que shopping_trends.csv existe
if [ ! -f "shopping_trends.csv" ]; then
    echo "⚠️  Advertencia: No se encontró shopping_trends.csv"
    echo "Asegúrate de tener el archivo CSV en el directorio proyecto/"
    echo ""
fi

echo "=========================================="
echo "  ✅ Instalación completada con éxito"
echo "=========================================="
echo ""
echo "Para iniciar el servidor:"
echo "  1. Activa el entorno virtual (si no está activado):"
echo "     source venv/bin/activate"
echo ""
echo "  2. Ejecuta el servidor:"
echo "     python manage.py runserver"
echo ""
echo "  3. Abre tu navegador en:"
echo "     http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/"
echo ""
echo "Para desactivar el entorno virtual:"
echo "     deactivate"
echo ""

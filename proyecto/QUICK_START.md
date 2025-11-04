# 🚀 Guía de Inicio Rápido

## Instalación en 3 Pasos

### Linux/Mac
```bash
cd proyecto/
./install.sh
python manage.py runserver
```

### Windows
```cmd
cd proyecto
install.bat
python manage.py runserver
```

### Manual
```bash
pip install django pandas
python manage.py migrate
python manage.py runserver
```

## 📊 Acceder al Dashboard

Abre tu navegador en: **http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/**

## 📁 Archivos Importantes

- 📖 **README_SHOPPING_TRENDS.md** - Documentación completa
- 📊 **GRAFICOS_RESUMEN.md** - Descripción de cada gráfico
- 📝 **CAMBIOS_REALIZADOS.md** - Changelog detallado
- 📋 **requirements.txt** - Dependencias

## 🎨 16 Gráficos Disponibles

### Datos Académicos (1-4)
1. Total Alumnos
2. Total por Secciones
3. Promedio Nota 1
4. Promedio TVD

### Shopping Trends (5-16)
5. Histograma Poder Adquisitivo
6. Histograma Edad
7. Clientes por Género
8. Métodos de Pago
9. Frecuencia de Compras
10. Edad vs. Monto (Scatter)
11. Poder Adquisitivo por Género
12. Categoría vs. Monto
13. Método Pago vs. Monto
14. Temporada vs. Cantidad (Línea)
15. Ubicación vs. Cantidad (Horizontal)
16. Temporada y Método Pago (Agrupado)

## 🛠️ Tecnologías

- **Backend**: Django + Pandas
- **Frontend**: Chart.js + Bootstrap
- **Dataset**: shopping_trends.csv (3,900 registros)

## ✅ Requisitos

- Python 3.8+
- Django 4.2+
- Pandas 2.0+
- Archivo shopping_trends.csv

## 🆘 Problemas Comunes

**Error: No module named 'django'**
```bash
pip install django pandas
```

**Error: Can't find shopping_trends.csv**
- Verifica que esté en el directorio `proyecto/`

**Los gráficos no cargan**
- Necesitas conexión a internet (Chart.js desde CDN)

## 📞 Más Información

Lee **README_SHOPPING_TRENDS.md** para documentación completa.

---

**¡Listo para usar! 🎉**
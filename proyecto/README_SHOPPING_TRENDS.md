# Dashboard de Shopping Trends - Proyecto Django

Este proyecto Django contiene visualizaciones interactivas de los datos de `shopping_trends.csv` utilizando Chart.js.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Crear y activar entorno virtual (recomendado)

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install django pandas
```

## Estructura del Proyecto

```
proyecto/
├── manage.py
├── shopping_trends.csv          # Dataset de tendencias de compras
├── GraficosVisualizacion.ipynb  # Notebook original con análisis
├── app_datos/
│   ├── views.py                 # Vistas con lógica de procesamiento
│   ├── urls.py                  # Rutas de la aplicación
│   └── templates/
│       ├── base.html            # Template base con menú
│       └── shopping/            # Templates de gráficos
│           ├── histograma_poder_adquisitivo.html
│           ├── histograma_edad.html
│           ├── clientes_por_genero.html
│           ├── metodos_pago.html
│           ├── frecuencia_compras.html
│           ├── edad_vs_monto.html
│           ├── poder_adquisitivo_genero.html
│           ├── categoria_vs_monto.html
│           ├── metodo_pago_vs_monto.html
│           ├── temporada_vs_cantidad.html
│           ├── ubicacion_vs_cantidad.html
│           └── temporada_metodo_pago.html
└── proyecto/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Ejecución del Proyecto

### 1. Ejecutar migraciones (primera vez)

```bash
python manage.py migrate
```

### 2. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

### 3. Acceder al dashboard

Abre tu navegador y visita:
```
http://127.0.0.1:8000/datos/total-alumnos/
```

O directamente a cualquier gráfico de shopping trends:
```
http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/
```

## Gráficos Disponibles

### Datos Académicos (originales)
1. **Total Alumnos** - Contador simple
2. **Total por Secciones** - Gráfico de barras
3. **Promedio Nota 1 (Ramos)** - Gráfico de barras
4. **Promedio TVD (Secciones)** - Gráfico de barras

### Shopping Trends (nuevos)
5. **Histograma Poder Adquisitivo** - Distribución de montos de compra
6. **Histograma Edad** - Distribución por edad de clientes
7. **Clientes por Género** - Comparación de género de clientes
8. **Métodos de Pago** - Preferencias de métodos de pago
9. **Frecuencia de Compras** - Intervalos de compra de clientes
10. **Edad vs. Monto** - Gráfico scatter de correlación
11. **Poder Adquisitivo por Género** - Comparación con estadísticas detalladas
12. **Categoría vs. Monto** - Análisis por categoría de producto
13. **Método Pago vs. Monto** - Promedio de compra por método de pago
14. **Temporada vs. Cantidad** - Tendencias estacionales (gráfico de línea)
15. **Ubicación vs. Cantidad** - Análisis geográfico (barras horizontales)
16. **Temporada y Método Pago** - Análisis combinado (barras agrupadas)

## Tecnologías Utilizadas

- **Backend**: Django 4.x
- **Procesamiento de Datos**: Pandas
- **Visualización**: Chart.js 4.x
- **Frontend**: Bootstrap 5.3.3
- **Dataset**: shopping_trends.csv (3900 registros)

## Características de los Gráficos

- ✅ Todos los gráficos son **interactivos** con Chart.js
- ✅ Tooltips informativos al pasar el mouse
- ✅ Diseño responsive con Bootstrap
- ✅ Colores pastel consistentes con el notebook original
- ✅ Estadísticas detalladas en tablas (donde aplica)
- ✅ Navegación por sidebar con scroll

## Notas Técnicas

### Conversión de Boxplots
Los gráficos de boxplot del notebook (matplotlib/seaborn) se convirtieron a:
- Gráficos de barras comparativos (media vs mediana)
- Tablas con estadísticas detalladas (min, Q1, mediana, Q3, max)
- Tooltips con información completa de distribución

### Procesamiento de Datos
- Los datos se procesan en tiempo real desde el CSV
- Se utiliza Pandas para agregaciones y estadísticas
- Los datos se pasan como JSON a los templates para Chart.js

### Paleta de Colores
Se utilizan colores pastel consistentes:
- Rosa: `rgba(255, 182, 193, 0.7)`
- Azul claro: `rgba(173, 216, 230, 0.7)`
- Durazno: `rgba(255, 228, 181, 0.7)`
- Lavanda: `rgba(221, 160, 221, 0.7)`
- Verde claro: `rgba(144, 238, 144, 0.7)`
- Naranja claro: `rgba(255, 218, 185, 0.7)`

## Solución de Problemas

### Error: ModuleNotFoundError: No module named 'django'
```bash
pip install django pandas
```

### Error: No such file or directory: 'shopping_trends.csv'
Asegúrate de que el archivo `shopping_trends.csv` esté en el directorio `proyecto/` (mismo nivel que `manage.py`)

### Los gráficos no se muestran
1. Verifica que tengas conexión a internet (Chart.js se carga desde CDN)
2. Revisa la consola del navegador (F12) para errores JavaScript

## Autor

Proyecto desarrollado para el curso de Visualización de Datos - UDD 2025

---

**Última actualización**: Noviembre 2024
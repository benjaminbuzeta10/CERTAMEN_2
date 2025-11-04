# 🔗 URLs de Acceso - Dashboard Shopping Trends

## 📍 URL Base del Servidor

```
http://127.0.0.1:8000
```

---

## 📊 Datos Académicos

### 1. Total Alumnos
```
http://127.0.0.1:8000/datos/total-alumnos/
```

### 2. Total por Secciones
```
http://127.0.0.1:8000/datos/total-secciones/
```

### 3. Promedio Nota 1 (Ramos)
```
http://127.0.0.1:8000/datos/notas1-ramos/
```

### 4. Promedio TVD (Secciones)
```
http://127.0.0.1:8000/datos/promedio-tvd/
```

---

## 🛍️ Shopping Trends

### 5. Histograma de Poder Adquisitivo
```
http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/
```
**Descripción**: Distribución de montos de compra en 15 intervalos

### 6. Histograma de Edad
```
http://127.0.0.1:8000/datos/shopping/histograma-edad/
```
**Descripción**: Distribución de edades de clientes en 10 intervalos

### 7. Clientes por Género
```
http://127.0.0.1:8000/datos/shopping/clientes-por-genero/
```
**Descripción**: Comparación de cantidad de clientes por género

### 8. Métodos de Pago
```
http://127.0.0.1:8000/datos/shopping/metodos-pago/
```
**Descripción**: Frecuencia de uso de cada método de pago

### 9. Frecuencia de Compras
```
http://127.0.0.1:8000/datos/shopping/frecuencia-compras/
```
**Descripción**: Distribución de clientes según su frecuencia de compra

### 10. Edad vs. Monto de Compra
```
http://127.0.0.1:8000/datos/shopping/edad-vs-monto/
```
**Descripción**: Gráfico de dispersión mostrando correlación edad-monto

### 11. Poder Adquisitivo por Género
```
http://127.0.0.1:8000/datos/shopping/poder-adquisitivo-genero/
```
**Descripción**: Análisis estadístico completo de compras por género

### 12. Categoría vs. Monto de Compra
```
http://127.0.0.1:8000/datos/shopping/categoria-vs-monto/
```
**Descripción**: Análisis de compras por categoría de producto

### 13. Método de Pago vs. Monto de Compra
```
http://127.0.0.1:8000/datos/shopping/metodo-pago-vs-monto/
```
**Descripción**: Promedio de compra según método de pago

### 14. Temporada vs. Cantidad Comprada
```
http://127.0.0.1:8000/datos/shopping/temporada-vs-cantidad/
```
**Descripción**: Tendencias de ventas por temporada (gráfico de línea)

### 15. Ubicación vs. Cantidad Comprada
```
http://127.0.0.1:8000/datos/shopping/ubicacion-vs-cantidad/
```
**Descripción**: Análisis geográfico de compras por estado

### 16. Temporada y Método de Pago
```
http://127.0.0.1:8000/datos/shopping/temporada-metodo-pago/
```
**Descripción**: Análisis combinado de ventas por temporada y método de pago

---

## 🎯 Acceso Rápido (Copiar y Pegar)

### Abrir Todos los Gráficos de Shopping Trends

**Linux/Mac (Terminal)**
```bash
# Abrir en el navegador predeterminado
open http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/
```

**Windows (CMD)**
```cmd
start http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/
```

**Windows (PowerShell)**
```powershell
Start-Process "http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/"
```

---

## 📋 Lista de URLs para Testing

### Todas las URLs de Shopping Trends
```
/datos/shopping/histograma-poder-adquisitivo/
/datos/shopping/histograma-edad/
/datos/shopping/clientes-por-genero/
/datos/shopping/metodos-pago/
/datos/shopping/frecuencia-compras/
/datos/shopping/edad-vs-monto/
/datos/shopping/poder-adquisitivo-genero/
/datos/shopping/categoria-vs-monto/
/datos/shopping/metodo-pago-vs-monto/
/datos/shopping/temporada-vs-cantidad/
/datos/shopping/ubicacion-vs-cantidad/
/datos/shopping/temporada-metodo-pago/
```

---

## 🧪 Prueba de URLs (cURL)

### Verificar que el servidor responda
```bash
curl -I http://127.0.0.1:8000/datos/shopping/histograma-poder-adquisitivo/
```

### Verificar todas las URLs
```bash
for url in histograma-poder-adquisitivo histograma-edad clientes-por-genero metodos-pago frecuencia-compras edad-vs-monto poder-adquisitivo-genero categoria-vs-monto metodo-pago-vs-monto temporada-vs-cantidad ubicacion-vs-cantidad temporada-metodo-pago; do
  echo "Testing: /datos/shopping/$url/"
  curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8000/datos/shopping/$url/
done
```

---

## 🗺️ Mapa de Navegación

```
Dashboard Principal
│
├── Datos Académicos
│   ├── Total Alumnos
│   ├── Total por Secciones
│   ├── Promedio Nota 1
│   └── Promedio TVD
│
└── Shopping Trends
    ├── Distribuciones
    │   ├── Histograma Poder Adquisitivo
    │   └── Histograma Edad
    │
    ├── Comparaciones Simples
    │   ├── Clientes por Género
    │   ├── Métodos de Pago
    │   └── Frecuencia de Compras
    │
    ├── Análisis Avanzados
    │   ├── Edad vs. Monto (Scatter)
    │   ├── Poder Adquisitivo por Género
    │   └── Categoría vs. Monto
    │
    └── Tendencias
        ├── Método Pago vs. Monto
        ├── Temporada vs. Cantidad
        ├── Ubicación vs. Cantidad
        └── Temporada y Método Pago
```

---

## 🔧 Configuración de URLs en Django

**Archivo**: `app_datos/urls.py`

```python
urlpatterns = [
    # Académicos
    path('total-alumnos/', views.total_alumnos, name='total_alumnos'),
    
    # Shopping Trends
    path('shopping/histograma-poder-adquisitivo/', 
         views.histograma_poder_adquisitivo, 
         name='histograma_poder_adquisitivo'),
    # ... más rutas
]
```

**Archivo**: `proyecto/urls.py`

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('datos/', include('app_datos.urls')),
]
```

---

## 📝 Notas

- Todas las URLs requieren que el servidor Django esté corriendo
- El puerto por defecto es 8000, pero puede cambiar si está ocupado
- Si el puerto cambia, Django te informará en la consola
- Las URLs son case-sensitive en producción

---

**Última actualización**: Noviembre 2024
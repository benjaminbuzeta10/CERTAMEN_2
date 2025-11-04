# Resumen de Gráficos - Dashboard Shopping Trends

Este documento describe cada uno de los gráficos implementados en el dashboard, explicando qué muestra, qué tipo de gráfico es y qué insights proporciona.

---

## Datos Académicos (Gráficos Originales)

### 1. Total Alumnos
- **Tipo**: Contador / Métrica
- **Descripción**: Muestra el número total de alumnos registrados en el sistema
- **Insight**: Vista rápida del tamaño de la población estudiantil (210 alumnos)

### 2. Total por Secciones
- **Tipo**: Gráfico de Barras
- **Descripción**: Distribución de alumnos por cada sección (A-G)
- **Insight**: Permite identificar qué secciones tienen más o menos alumnos

### 3. Promedio Nota 1 (Ramos)
- **Tipo**: Gráfico de Barras
- **Descripción**: Promedio de la primera nota de cada ramo
- **Insight**: Compara el rendimiento inicial de los estudiantes en diferentes materias

### 4. Promedio TVD (Secciones)
- **Tipo**: Gráfico de Barras
- **Descripción**: Promedio de la nota 1 de TVD por cada sección
- **Insight**: Identifica qué secciones tienen mejor rendimiento en Visualización de Datos

---

## Shopping Trends (Nuevos Gráficos)

### 5. Histograma de Poder Adquisitivo
- **URL**: `/datos/shopping/histograma-poder-adquisitivo/`
- **Tipo**: Histograma (Gráfico de Barras con bins)
- **Fuente**: Campo `Purchase Amount (USD)`
- **Descripción**: Distribución de los montos de compra en 15 intervalos
- **Insights**:
  - Rango de compras: $20 - $100
  - Identificar el rango de precios más común
  - Detectar patrones en el comportamiento de compra

### 6. Histograma de Edad
- **URL**: `/datos/shopping/histograma-edad/`
- **Tipo**: Histograma (Gráfico de Barras con bins)
- **Fuente**: Campo `Age`
- **Descripción**: Distribución de edades de los clientes en 10 intervalos
- **Insights**:
  - Rango de edades: 18 - 70 años
  - Identificar el grupo etario más numeroso
  - Segmentación demográfica de clientes

### 7. Clientes por Género
- **URL**: `/datos/shopping/clientes-por-genero/`
- **Tipo**: Gráfico de Barras
- **Fuente**: Campo `Gender`
- **Descripción**: Cantidad de clientes masculinos vs femeninos
- **Insights**:
  - Balance de género en la base de clientes
  - Identificar el género predominante
  - Base para estrategias de marketing segmentado

### 8. Métodos de Pago
- **URL**: `/datos/shopping/metodos-pago/`
- **Tipo**: Gráfico de Barras
- **Fuente**: Campo `Payment Method`
- **Descripción**: Frecuencia de uso de cada método de pago
- **Métodos**: Credit Card, PayPal, Venmo, Cash, Bank Transfer, Debit Card
- **Insights**:
  - Método de pago más popular
  - Métodos menos utilizados (considerar eliminar)
  - Optimización de opciones de pago

### 9. Frecuencia de Compras
- **URL**: `/datos/shopping/frecuencia-compras/`
- **Tipo**: Gráfico de Barras
- **Fuente**: Campo `Frequency of Purchases`
- **Descripción**: Distribución de clientes según su frecuencia de compra
- **Categorías**: Weekly, Fortnightly, Monthly, Bi-Weekly, Quarterly, Annually, Every 3 Months
- **Insights**:
  - Identificar clientes más frecuentes
  - Patrones de lealtad del cliente
  - Oportunidades para programas de fidelización

### 10. Edad vs. Monto de Compra
- **URL**: `/datos/shopping/edad-vs-monto/`
- **Tipo**: Gráfico de Dispersión (Scatter Plot)
- **Fuentes**: `Age` (eje X) y `Purchase Amount (USD)` (eje Y)
- **Descripción**: Relación entre la edad del cliente y su promedio de compra
- **Insights**:
  - Correlación entre edad y poder adquisitivo
  - Identificar grupos etarios con mayor gasto
  - Segmentación de mercado por edad y capacidad de compra

### 11. Poder Adquisitivo por Género
- **URL**: `/datos/shopping/poder-adquisitivo-genero/`
- **Tipo**: Gráfico de Barras Comparativo + Tabla de Estadísticas
- **Fuentes**: `Gender` y `Purchase Amount (USD)`
- **Descripción**: Compara la distribución de compras entre géneros
- **Estadísticas mostradas**:
  - Mínimo, Q1 (25%), Mediana, Media, Q3 (75%), Máximo
- **Insights**:
  - Diferencias en el gasto entre géneros
  - Identificar cuál género gasta más en promedio
  - Dispersión del gasto por género

### 12. Categoría vs. Monto de Compra
- **URL**: `/datos/shopping/categoria-vs-monto/`
- **Tipo**: Gráfico de Barras Comparativo + Tabla de Estadísticas
- **Fuentes**: `Category` y `Purchase Amount (USD)`
- **Descripción**: Compara el gasto promedio por categoría de producto
- **Categorías**: Clothing, Footwear, Accessories, Outerwear
- **Estadísticas mostradas**:
  - Mínimo, Q1, Mediana, Media, Q3, Máximo por categoría
- **Insights**:
  - Categoría más rentable
  - Variabilidad de precios por categoría
  - Oportunidades de pricing

### 13. Método de Pago vs. Monto de Compra
- **URL**: `/datos/shopping/metodo-pago-vs-monto/`
- **Tipo**: Gráfico de Barras
- **Fuentes**: `Payment Method` y `Purchase Amount (USD)`
- **Descripción**: Promedio de compra según el método de pago utilizado
- **Insights**:
  - Métodos de pago asociados a compras más grandes
  - Comportamiento de gasto según forma de pago
  - Incentivar métodos de pago preferidos

### 14. Temporada vs. Cantidad Comprada
- **URL**: `/datos/shopping/temporada-vs-cantidad/`
- **Tipo**: Gráfico de Líneas
- **Fuentes**: `Season` y `Purchase Amount (USD)` (suma total)
- **Descripción**: Tendencia de ventas totales a través de las temporadas
- **Temporadas**: Winter → Spring → Summer → Fall
- **Insights**:
  - Temporada con mayor volumen de ventas
  - Temporada baja para planificar promociones
  - Ciclos estacionales de negocio

### 15. Ubicación vs. Cantidad Comprada
- **URL**: `/datos/shopping/ubicacion-vs-cantidad/`
- **Tipo**: Gráfico de Barras Horizontales
- **Fuentes**: `Location` y `Purchase Amount (USD)`
- **Descripción**: Promedio de compra por estado (50 estados de EE.UU.)
- **Insights**:
  - Estados con mayor poder adquisitivo
  - Expansión geográfica del negocio
  - Identificar mercados premium
  - Optimización de inventario por región

### 16. Temporada y Método de Pago
- **URL**: `/datos/shopping/temporada-metodo-pago/`
- **Tipo**: Gráfico de Barras Agrupadas
- **Fuentes**: `Season`, `Payment Method` y `Purchase Amount (USD)`
- **Descripción**: Análisis combinado de ventas por temporada y método de pago
- **Insights**:
  - Métodos de pago preferidos por temporada
  - Patrones estacionales en formas de pago
  - Optimización de opciones de pago por época
  - Promociones específicas por temporada y método

---

## Tecnología de Visualización

Todos los gráficos utilizan **Chart.js 4.x**, una biblioteca JavaScript moderna para crear gráficos interactivos con las siguientes características:

### Características Implementadas:
- ✅ **Interactividad**: Hover para ver datos exactos
- ✅ **Tooltips personalizados**: Información contextual al pasar el mouse
- ✅ **Diseño responsive**: Se adaptan a cualquier tamaño de pantalla
- ✅ **Animaciones suaves**: Transiciones visuales agradables
- ✅ **Paleta de colores consistente**: Colores pastel profesionales
- ✅ **Etiquetas claras**: Ejes y títulos descriptivos
- ✅ **Leyendas informativas**: Fácil interpretación de datos

### Tipos de Gráficos Utilizados:
1. **Bar Chart** (Barras verticales): 9 gráficos
2. **Horizontal Bar Chart** (Barras horizontales): 1 gráfico
3. **Line Chart** (Líneas): 1 gráfico
4. **Scatter Plot** (Dispersión): 1 gráfico

---

## Procesamiento de Datos

El procesamiento de datos se realiza con **Pandas** en el backend de Django:

### Operaciones Realizadas:
- **Agrupaciones**: `groupby()` para análisis por categorías
- **Estadísticas**: `mean()`, `sum()`, `quantile()` para métricas
- **Conteos**: `value_counts()` para frecuencias
- **Bins**: `pd.cut()` para crear histogramas
- **Ordenamiento**: `sort_values()` para rankings

### Flujo de Datos:
1. CSV → Pandas DataFrame
2. Procesamiento y agregación
3. Conversión a JSON
4. Paso a template Django
5. Renderizado con Chart.js

---

## Dataset: shopping_trends.csv

### Información General:
- **Registros**: 3,900 transacciones
- **Columnas**: 18 campos
- **Período**: Datos sintéticos de tendencias de compra

### Campos Principales:
1. **Customer ID**: ID único del cliente (1-3900)
2. **Age**: Edad del cliente (18-70)
3. **Gender**: Género (Male, Female)
4. **Item Purchased**: Producto comprado (25 tipos)
5. **Category**: Categoría (Clothing, Footwear, Accessories, Outerwear)
6. **Purchase Amount (USD)**: Monto ($20-$100)
7. **Location**: Estado de EE.UU. (50 estados)
8. **Size**: Talla (S, M, L, XL)
9. **Color**: Color del producto (25 colores)
10. **Season**: Temporada (Winter, Spring, Summer, Fall)
11. **Review Rating**: Calificación (2.5-5.0)
12. **Subscription Status**: Suscrito (Yes/No)
13. **Shipping Type**: Tipo de envío (6 tipos)
14. **Discount Applied**: Descuento aplicado (Yes/No)
15. **Promo Code Used**: Código promocional (Yes/No)
16. **Previous Purchases**: Compras previas (1-50)
17. **Payment Method**: Método de pago (6 métodos)
18. **Frequency of Purchases**: Frecuencia (7 categorías)

---

## Valor Analítico

Estos gráficos proporcionan información valiosa para:

### 1. Estrategia de Marketing
- Segmentación demográfica precisa
- Identificación de clientes objetivo
- Personalización de campañas

### 2. Optimización de Inventario
- Productos más vendidos por temporada
- Demanda por ubicación geográfica
- Preferencias por categoría

### 3. Experiencia del Cliente
- Métodos de pago preferidos
- Frecuencia de compra para programas de lealtad
- Patrones de comportamiento

### 4. Decisiones de Negocio
- Identificación de mercados premium
- Temporadas óptimas para promociones
- Categorías con mayor margen

---

**Última actualización**: Noviembre 2024
**Autor**: Proyecto Visualización de Datos - UDD
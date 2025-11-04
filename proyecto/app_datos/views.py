from django.shortcuts import render
import random
import pandas as pd
import os
from django.conf import settings

# Create your views here.

RAMOS = ["TVD", "BD", "POO", "ML", "AWS"]
SECCIONES = ["A", "B", "C", "D", "E", "F", "G"]
TOTAL_ALUMNOS = 210

lista_alumnos = []

for i in range(1, TOTAL_ALUMNOS + 1):
    notas_alumno = {}
    for ramo in RAMOS:
        notas_alumno[ramo] = {
            "nota1": round(random.uniform(1.0, 7.0), 1),
            "nota2": round(random.uniform(1.0, 7.0), 1),
            "nota3": round(random.uniform(1.0, 7.0), 1),
        }

    Alumno = {"id": i, "seccion": random.choice(SECCIONES), "notas": notas_alumno}

    lista_alumnos.append(Alumno)


# Cargar datos de shopping trends
def load_shopping_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "shopping_trends.csv")
    return pd.read_csv(csv_path)


def dashboard_home(request):
    # Definir todos los gráficos con su información
    graficos = [
        {
            "id": 1,
            "titulo": "Total Alumnos",
            "descripcion": "Contador total de alumnos",
            "categoria": "Académico",
            "url": "total_alumnos",
            "color": "primary",
        },
        {
            "id": 2,
            "titulo": "Total por Secciones",
            "descripcion": "Distribución por sección",
            "categoria": "Académico",
            "url": "total_secciones",
            "color": "info",
        },
        {
            "id": 3,
            "titulo": "Promedio Nota 1",
            "descripcion": "Promedio por ramos",
            "categoria": "Académico",
            "url": "notas1_ramos",
            "color": "success",
        },
        {
            "id": 4,
            "titulo": "Promedio TVD",
            "descripcion": "TVD por secciones",
            "categoria": "Académico",
            "url": "promedio_tvd",
            "color": "warning",
        },
        {
            "id": 5,
            "titulo": "Histograma Poder Adquisitivo",
            "descripcion": "Distribución de montos de compra",
            "categoria": "Shopping",
            "url": "histograma_poder_adquisitivo",
            "color": "danger",
        },
        {
            "id": 6,
            "titulo": "Histograma Edad",
            "descripcion": "Distribución por edad",
            "categoria": "Shopping",
            "url": "histograma_edad",
            "color": "secondary",
        },
        {
            "id": 7,
            "titulo": "Clientes por Género",
            "descripcion": "Comparación de género",
            "categoria": "Shopping",
            "url": "clientes_por_genero",
            "color": "primary",
        },
        {
            "id": 8,
            "titulo": "Métodos de Pago",
            "descripcion": "Preferencias de pago",
            "categoria": "Shopping",
            "url": "metodos_pago",
            "color": "info",
        },
        {
            "id": 9,
            "titulo": "Frecuencia de Compras",
            "descripcion": "Patrones de compra",
            "categoria": "Shopping",
            "url": "frecuencia_compras",
            "color": "success",
        },
        {
            "id": 10,
            "titulo": "Edad vs. Monto",
            "descripcion": "Correlación edad-monto",
            "categoria": "Shopping",
            "url": "edad_vs_monto",
            "color": "warning",
        },
        {
            "id": 11,
            "titulo": "Poder Adquisitivo por Género",
            "descripcion": "Análisis estadístico por género",
            "categoria": "Shopping",
            "url": "poder_adquisitivo_genero",
            "color": "danger",
        },
        {
            "id": 12,
            "titulo": "Categoría vs. Monto",
            "descripcion": "Análisis por categoría",
            "categoria": "Shopping",
            "url": "categoria_vs_monto",
            "color": "secondary",
        },
        {
            "id": 13,
            "titulo": "Método Pago vs. Monto",
            "descripcion": "Promedio por método de pago",
            "categoria": "Shopping",
            "url": "metodo_pago_vs_monto",
            "color": "primary",
        },
        {
            "id": 14,
            "titulo": "Temporada vs. Cantidad",
            "descripcion": "Tendencias estacionales",
            "categoria": "Shopping",
            "url": "temporada_vs_cantidad",
            "color": "info",
        },
        {
            "id": 15,
            "titulo": "Ubicación vs. Cantidad",
            "descripcion": "Análisis geográfico",
            "categoria": "Shopping",
            "url": "ubicacion_vs_cantidad",
            "color": "success",
        },
        {
            "id": 16,
            "titulo": "Temporada y Método Pago",
            "descripcion": "Análisis combinado",
            "categoria": "Shopping",
            "url": "temporada_metodo_pago",
            "color": "warning",
        },
    ]

    context = {"graficos": graficos}
    return render(request, "dashboard_home.html", context)


def menu(request):
    return render(request, "base.html")


def total_alumnos(request):
    total = len(lista_alumnos)

    context = {"total_alumnos": total}

    return render(request, "total_alumnos.html", context)


def total_secciones(request):
    conteo_secciones = {sec: 0 for sec in SECCIONES}

    for alumno in lista_alumnos:
        seccion = alumno["seccion"]
        conteo_secciones[seccion] += 1

    context = {
        "labels": list(conteo_secciones.keys()),
        "data": list(conteo_secciones.values()),
    }

    return render(request, "total_secciones.html", context)


def notas1_ramos(request):
    promedios = {ramo: 0 for ramo in RAMOS}

    for alumno in lista_alumnos:
        for ramo in RAMOS:
            promedios[ramo] += alumno["notas"][ramo]["nota1"]

    for ramo in RAMOS:
        promedios[ramo] = round(promedios[ramo] / TOTAL_ALUMNOS, 2)

    context = {"labels": list(promedios.keys()), "data": list(promedios.values())}

    return render(request, "notas1.html", context)


def promedio_tvd_seccion(request):
    stats_tvd = {sec: {"suma": 0, "conteo": 0} for sec in SECCIONES}

    for alumno in lista_alumnos:
        seccion = alumno["seccion"]
        nota_tvd_1 = alumno["notas"]["TVD"]["nota1"]

        stats_tvd[seccion]["suma"] += nota_tvd_1
        stats_tvd[seccion]["conteo"] += 1

    promedios_finales = {}
    for seccion in SECCIONES:
        suma = stats_tvd[seccion]["suma"]
        conteo = stats_tvd[seccion]["conteo"]

        if conteo > 0:
            promedios_finales[seccion] = round(suma / conteo, 2)
        else:
            promedios_finales[seccion] = 0.0

    context = {
        "labels": list(promedios_finales.keys()),
        "data": list(promedios_finales.values()),
    }

    return render(request, "promedio_tvd.html", context)


# ========== VISTAS PARA SHOPPING TRENDS ==========


# 1. Histograma de Poder Adquisitivo (USD)
def histograma_poder_adquisitivo(request):
    df = load_shopping_data()

    # Crear bins para el histograma
    bins = pd.cut(df["Purchase Amount (USD)"], bins=15)
    hist_data = bins.value_counts().sort_index()

    labels = [
        f"{int(interval.left)}-{int(interval.right)}" for interval in hist_data.index
    ]
    values = hist_data.values.tolist()

    context = {"labels": labels, "data": values}
    return render(request, "shopping/histograma_poder_adquisitivo.html", context)


# 2. Histograma de Edad
def histograma_edad(request):
    df = load_shopping_data()

    # Crear bins para el histograma
    bins = pd.cut(df["Age"], bins=10)
    hist_data = bins.value_counts().sort_index()

    labels = [
        f"{int(interval.left)}-{int(interval.right)}" for interval in hist_data.index
    ]
    values = hist_data.values.tolist()

    context = {"labels": labels, "data": values}
    return render(request, "shopping/histograma_edad.html", context)


# 3. Cantidad de clientes por Género
def clientes_por_genero(request):
    df = load_shopping_data()

    gender_counts = df["Gender"].value_counts()

    context = {
        "labels": gender_counts.index.tolist(),
        "data": gender_counts.values.tolist(),
    }
    return render(request, "shopping/clientes_por_genero.html", context)


# 4. Preferencia de métodos de pago
def metodos_pago(request):
    df = load_shopping_data()

    payment_counts = df["Payment Method"].value_counts()

    context = {
        "labels": payment_counts.index.tolist(),
        "data": payment_counts.values.tolist(),
    }
    return render(request, "shopping/metodos_pago.html", context)


# 5. Frecuencia de compras por cliente
def frecuencia_compras(request):
    df = load_shopping_data()

    frequency_counts = df["Frequency of Purchases"].value_counts()

    context = {
        "labels": frequency_counts.index.tolist(),
        "data": frequency_counts.values.tolist(),
    }
    return render(request, "shopping/frecuencia_compras.html", context)


# 6. Edad vs. Monto de Compra (scatter)
def edad_vs_monto(request):
    df = load_shopping_data()

    # Agrupar por edad y calcular promedio
    edad_monto = df.groupby("Age")["Purchase Amount (USD)"].mean().reset_index()

    context = {
        "ages": edad_monto["Age"].tolist(),
        "amounts": edad_monto["Purchase Amount (USD)"].round(2).tolist(),
    }
    return render(request, "shopping/edad_vs_monto.html", context)


# 7. Poder Adquisitivo vs. Género (boxplot simulado con estadísticas)
def poder_adquisitivo_genero(request):
    df = load_shopping_data()

    # Calcular estadísticas por género
    stats = {}
    for gender in df["Gender"].unique():
        data = df[df["Gender"] == gender]["Purchase Amount (USD)"]
        stats[gender] = {
            "min": float(data.min()),
            "q1": float(data.quantile(0.25)),
            "median": float(data.median()),
            "q3": float(data.quantile(0.75)),
            "max": float(data.max()),
            "mean": float(data.mean()),
        }

    context = {"stats": stats}
    return render(request, "shopping/poder_adquisitivo_genero.html", context)


# 8. Categoría Artículo vs. Monto de Compra
def categoria_vs_monto(request):
    df = load_shopping_data()

    # Calcular estadísticas por categoría
    stats = {}
    for category in df["Category"].unique():
        data = df[df["Category"] == category]["Purchase Amount (USD)"]
        stats[category] = {
            "min": float(data.min()),
            "q1": float(data.quantile(0.25)),
            "median": float(data.median()),
            "q3": float(data.quantile(0.75)),
            "max": float(data.max()),
            "mean": float(data.mean()),
        }

    context = {"stats": stats}
    return render(request, "shopping/categoria_vs_monto.html", context)


# 9. Método de Pago vs. Monto de Compra
def metodo_pago_vs_monto(request):
    df = load_shopping_data()

    # Calcular promedio por método de pago
    payment_avg = (
        df.groupby("Payment Method")["Purchase Amount (USD)"]
        .mean()
        .sort_values(ascending=False)
    )

    context = {
        "labels": payment_avg.index.tolist(),
        "data": payment_avg.round(2).values.tolist(),
    }
    return render(request, "shopping/metodo_pago_vs_monto.html", context)


# 10. Temporada vs. Cantidad Comprada (línea)
def temporada_vs_cantidad(request):
    df = load_shopping_data()

    # Ordenar por temporadas específicas
    season_order = ["Winter", "Spring", "Summer", "Fall"]
    season_sales = df.groupby("Season")["Purchase Amount (USD)"].sum()
    season_sales = season_sales.reindex(season_order)

    context = {"labels": season_order, "data": season_sales.values.tolist()}
    return render(request, "shopping/temporada_vs_cantidad.html", context)


# 11. Ubicación vs. Cantidad Comprada
def ubicacion_vs_cantidad(request):
    df = load_shopping_data()

    # Calcular promedio por ubicación y ordenar
    location_avg = (
        df.groupby("Location")["Purchase Amount (USD)"]
        .mean()
        .sort_values(ascending=False)
    )

    context = {
        "labels": location_avg.index.tolist(),
        "data": location_avg.round(2).values.tolist(),
    }
    return render(request, "shopping/ubicacion_vs_cantidad.html", context)


# 12. Cantidad comprada por Temporada y Método de Pago
def temporada_metodo_pago(request):
    df = load_shopping_data()

    # Ordenar por temporadas
    season_order = ["Winter", "Spring", "Summer", "Fall"]

    # Obtener métodos de pago únicos
    payment_methods = df["Payment Method"].unique().tolist()

    # Crear dataset para cada método de pago
    datasets = {}
    for method in payment_methods:
        method_data = (
            df[df["Payment Method"] == method]
            .groupby("Season")["Purchase Amount (USD)"]
            .sum()
        )
        method_data = method_data.reindex(season_order, fill_value=0)
        datasets[method] = method_data.values.tolist()

    context = {
        "labels": season_order,
        "payment_methods": payment_methods,
        "datasets": datasets,
    }
    return render(request, "shopping/temporada_metodo_pago.html", context)

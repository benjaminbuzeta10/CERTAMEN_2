from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard_home, name="dashboard_home"),
    path("total-alumnos/", views.total_alumnos, name="total_alumnos"),
    path("total-secciones/", views.total_secciones, name="total_secciones"),
    path("notas1-ramos/", views.notas1_ramos, name="notas1_ramos"),
    path("promedio-tvd/", views.promedio_tvd_seccion, name="promedio_tvd"),
    # Shopping Trends URLs
    path(
        "shopping/histograma-poder-adquisitivo/",
        views.histograma_poder_adquisitivo,
        name="histograma_poder_adquisitivo",
    ),
    path("shopping/histograma-edad/", views.histograma_edad, name="histograma_edad"),
    path(
        "shopping/clientes-por-genero/",
        views.clientes_por_genero,
        name="clientes_por_genero",
    ),
    path("shopping/metodos-pago/", views.metodos_pago, name="metodos_pago"),
    path(
        "shopping/frecuencia-compras/",
        views.frecuencia_compras,
        name="frecuencia_compras",
    ),
    path("shopping/edad-vs-monto/", views.edad_vs_monto, name="edad_vs_monto"),
    path(
        "shopping/poder-adquisitivo-genero/",
        views.poder_adquisitivo_genero,
        name="poder_adquisitivo_genero",
    ),
    path(
        "shopping/categoria-vs-monto/",
        views.categoria_vs_monto,
        name="categoria_vs_monto",
    ),
    path(
        "shopping/metodo-pago-vs-monto/",
        views.metodo_pago_vs_monto,
        name="metodo_pago_vs_monto",
    ),
    path(
        "shopping/temporada-vs-cantidad/",
        views.temporada_vs_cantidad,
        name="temporada_vs_cantidad",
    ),
    path(
        "shopping/ubicacion-vs-cantidad/",
        views.ubicacion_vs_cantidad,
        name="ubicacion_vs_cantidad",
    ),
    path(
        "shopping/temporada-metodo-pago/",
        views.temporada_metodo_pago,
        name="temporada_metodo_pago",
    ),
]

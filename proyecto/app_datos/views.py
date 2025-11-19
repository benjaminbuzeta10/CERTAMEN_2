import csv
import io
import os
import random

import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    CategoryForm,
    ColorForm,
    CSVUploadForm,
    CustomerForm,
    LocationForm,
    PaymentMethodForm,
    ProductForm,
    PromotionForm,
    SeasonForm,
    ShippingTypeForm,
    SizeForm,
    TransactionForm,
)
from .models import (
    Categories,
    Colors,
    Customers,
    Locations,
    PaymentMethods,
    Products,
    Promotions,
    Seasons,
    ShippingTypes,
    Sizes,
    Transactions,
)

# Create your views here.


# Cargar datos de shopping trends
def load_shopping_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "shopping_trends.csv")
    return pd.read_csv(csv_path)


@login_required
def dashboard_home(request):
    # Obtener estadísticas de la base de datos del usuario actual
    total_customers = Customers.objects.filter(user=request.user).count()
    total_transactions = Transactions.objects.filter(user=request.user).count()
    total_products = Products.objects.filter(user=request.user).count()

    # Definir todos los gráficos con su información
    graficos = [
        {
            "id": 5,
            "titulo": "Histograma Poder Adquisitivo",
            "descripcion": "Distribución de montos de compra",
            "categoria": "Shopping",
            "url": "histograma_poder_adquisitivo",
            "color": "primary",
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

    context = {
        "graficos": graficos,
        "total_customers": total_customers,
        "total_transactions": total_transactions,
        "total_products": total_products,
    }
    return render(request, "dashboard_home.html", context)


def menu(request):
    return render(request, "base.html")


# VISTAS PARA SHOPPING TRENDS


# 1. Histograma de Poder Adquisitivo (USD)
@login_required
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
@login_required
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
@login_required
def clientes_por_genero(request):
    df = load_shopping_data()

    gender_counts = df["Gender"].value_counts()

    context = {
        "labels": gender_counts.index.tolist(),
        "data": gender_counts.values.tolist(),
    }
    return render(request, "shopping/clientes_por_genero.html", context)


# 4. Preferencia de métodos de pago
@login_required
def metodos_pago(request):
    df = load_shopping_data()

    payment_counts = df["Payment Method"].value_counts()

    context = {
        "labels": payment_counts.index.tolist(),
        "data": payment_counts.values.tolist(),
    }
    return render(request, "shopping/metodos_pago.html", context)


# 5. Frecuencia de compras por cliente
@login_required
def frecuencia_compras(request):
    df = load_shopping_data()

    frequency_counts = df["Frequency of Purchases"].value_counts()

    context = {
        "labels": frequency_counts.index.tolist(),
        "data": frequency_counts.values.tolist(),
    }
    return render(request, "shopping/frecuencia_compras.html", context)


# 6. Edad vs. Monto de Compra (scatter)
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
def temporada_vs_cantidad(request):
    df = load_shopping_data()

    # Ordenar por temporadas específicas
    season_order = ["Winter", "Spring", "Summer", "Fall"]
    season_sales = df.groupby("Season")["Purchase Amount (USD)"].sum()
    season_sales = season_sales.reindex(season_order)

    context = {"labels": season_order, "data": season_sales.values.tolist()}
    return render(request, "shopping/temporada_vs_cantidad.html", context)


# 11. Ubicación vs. Cantidad Comprada
@login_required
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
@login_required
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


# ==================== CRUD OPERATIONS ====================


# CUSTOMERS CRUD
@login_required
def customers_list(request):
    customers_list = Customers.objects.filter(user=request.user).order_by("id_customer")
    paginator = Paginator(customers_list, 400)  # Show 400 customers per page

    page_number = request.GET.get("page")
    customers = paginator.get_page(page_number)

    context = {"customers": customers}
    return render(request, "crud/customers_list.html", context)


@login_required
def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, "Cliente agregado exitosamente!")
            return redirect("customers_list")
        else:
            messages.error(request, "Error al agregar el cliente. Verifique los datos.")
    else:
        form = CustomerForm()

    context = {"form": form, "title": "Agregar Cliente"}
    return render(request, "crud/customer_form.html", context)


@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customers, id_customer=pk, user=request.user)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado exitosamente!")
            return redirect("customers_list")
        else:
            messages.error(request, "Error al actualizar el cliente.")
    else:
        form = CustomerForm(instance=customer)

    context = {"form": form, "title": "Editar Cliente", "customer": customer}
    return render(request, "crud/customer_form.html", context)


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customers, id_customer=pk, user=request.user)
    customer.delete()
    messages.success(request, "Cliente eliminado exitosamente!")
    return redirect("customers_list")


# TRANSACTIONS CRUD
@login_required
def transactions_list(request):
    transactions_list = (
        Transactions.objects.filter(user=request.user)
        .select_related("id_customer", "id_product", "id_paymentmethod", "id_shipping")
        .order_by("-id_transaction")
    )
    paginator = Paginator(transactions_list, 400)  # Show 400 transactions per page

    page_number = request.GET.get("page")
    transactions = paginator.get_page(page_number)

    context = {"transactions": transactions}
    return render(request, "crud/transactions_list.html", context)


@login_required
def transaction_add(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Transacción agregada exitosamente!")
            return redirect("transactions_list")
        else:
            messages.error(request, "Error al agregar la transacción.")
    else:
        form = TransactionForm()
        # Filter querysets to only show current user's data
        form.fields["id_customer"].queryset = Customers.objects.filter(
            user=request.user
        )
        form.fields["id_product"].queryset = Products.objects.filter(user=request.user)

    context = {"form": form, "title": "Agregar Transacción"}
    return render(request, "crud/transaction_form.html", context)


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transactions, id_transaction=pk, user=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Transacción actualizada exitosamente!")
            return redirect("transactions_list")
        else:
            messages.error(request, "Error al actualizar la transacción.")
    else:
        form = TransactionForm(instance=transaction)
        # Filter querysets to only show current user's data
        form.fields["id_customer"].queryset = Customers.objects.filter(
            user=request.user
        )
        form.fields["id_product"].queryset = Products.objects.filter(user=request.user)

    context = {"form": form, "title": "Editar Transacción", "transaction": transaction}
    return render(request, "crud/transaction_form.html", context)


@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transactions, id_transaction=pk, user=request.user)
    transaction.delete()
    messages.success(request, "Transacción eliminada exitosamente!")
    return redirect("transactions_list")


# PRODUCTS CRUD
@login_required
def products_list(request):
    products_list = (
        Products.objects.filter(user=request.user)
        .select_related("id_category", "id_size", "id_color", "id_season")
        .order_by("id_product")
    )
    paginator = Paginator(products_list, 400)  # Show 400 products per page

    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    context = {"products": products}
    return render(request, "crud/products_list.html", context)


@login_required
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, "Producto agregado exitosamente!")
            return redirect("products_list")
        else:
            messages.error(request, "Error al agregar el producto.")
    else:
        form = ProductForm()

    context = {"form": form, "title": "Agregar Producto"}
    return render(request, "crud/product_form.html", context)


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Products, id_product=pk, user=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado exitosamente!")
            return redirect("products_list")
        else:
            messages.error(request, "Error al actualizar el producto.")
    else:
        form = ProductForm(instance=product)

    context = {"form": form, "title": "Editar Producto", "product": product}
    return render(request, "crud/product_form.html", context)


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Products, id_product=pk, user=request.user)
    product.delete()
    messages.success(request, "Producto eliminado exitosamente!")
    return redirect("products_list")


# ==================== CSV UPLOAD ====================


@login_required
def csv_upload(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["csv_file"]

            # Verificar que sea un archivo CSV
            if not csv_file.name.endswith(".csv"):
                messages.error(request, "El archivo debe ser un CSV.")
                return redirect("csv_upload")

            try:
                # Leer el archivo CSV
                decoded_file = csv_file.read().decode("utf-8")
                io_string = io.StringIO(decoded_file)
                reader = csv.DictReader(io_string)

                # Contadores
                created_count = 0
                skipped_count = 0
                error_count = 0

                with transaction.atomic():
                    for row in reader:
                        try:
                            # Procesar cada fila del CSV
                            # 1. Obtener o crear ubicación
                            location, _ = Locations.objects.get_or_create(
                                state=row["Location"]
                            )

                            # 2. Obtener o crear método de pago
                            payment_method, _ = PaymentMethods.objects.get_or_create(
                                name=row["Payment Method"]
                            )

                            # 3. Obtener o crear preferred payment method
                            preferred_payment, _ = PaymentMethods.objects.get_or_create(
                                name=row["Preferred Payment Method"]
                            )

                            # 4. Verificar si el cliente ya existe (por edad, género, ubicación)
                            # Para evitar duplicados exactos
                            customer, created = Customers.objects.get_or_create(
                                user=request.user,
                                age=int(row["Age"]),
                                gender=row["Gender"],
                                id_location=location,
                                sub_status=row["Subscription Status"].lower() == "yes",
                                id_paymentmethod=preferred_payment,
                                freq_purchase=row["Frequency of Purchases"],
                                prev_purchases=int(row["Previous Purchases"]),
                            )

                            if not created:
                                skipped_count += 1
                                continue

                            # 5. Obtener o crear categoría
                            category, _ = Categories.objects.get_or_create(
                                name=row["Category"]
                            )

                            # 6. Obtener o crear talla
                            size, _ = Sizes.objects.get_or_create(
                                size_label=row["Size"]
                            )

                            # 7. Obtener o crear color
                            color, _ = Colors.objects.get_or_create(name=row["Color"])

                            # 8. Obtener o crear temporada
                            season, _ = Seasons.objects.get_or_create(
                                name=row["Season"]
                            )

                            # 9. Obtener o crear producto
                            product, _ = Products.objects.get_or_create(
                                user=request.user,
                                name=row["Item Purchased"],
                                defaults={
                                    "id_category": category,
                                    "id_size": size,
                                    "id_color": color,
                                    "id_season": season,
                                },
                            )

                            # 10. Obtener o crear tipo de envío
                            shipping_type, _ = ShippingTypes.objects.get_or_create(
                                name=row["Shipping Type"]
                            )

                            # 11. Crear promoción si se usó
                            promotion = None
                            if row["Promo Code Used"].lower() == "yes":
                                promotion, _ = Promotions.objects.get_or_create(
                                    promocode=f"PROMO_{row['Customer ID']}",
                                    defaults={"description": "Promoción aplicada"},
                                )

                            # 12. Crear transacción
                            Transactions.objects.create(
                                user=request.user,
                                id_customer=customer,
                                id_product=product,
                                purchase_amount=float(row["Purchase Amount (USD)"]),
                                review_rate=float(row["Review Rating"]),
                                id_paymentmethod=payment_method,
                                id_shipping=shipping_type,
                                dsct_applied=row["Discount Applied"].lower() == "yes",
                                promo_used=row["Promo Code Used"].lower() == "yes",
                                id_promotion=promotion,
                            )

                            created_count += 1

                        except Exception as e:
                            error_count += 1
                            print(f"Error procesando fila: {e}")
                            continue

                # Mensaje de éxito con estadísticas
                if created_count > 0:
                    messages.success(
                        request,
                        f"¡Carga completada! Registros creados: {created_count}, "
                        f"Duplicados omitidos: {skipped_count}, Errores: {error_count}",
                    )
                elif skipped_count > 0:
                    messages.warning(
                        request,
                        f"Todos los registros ya existían en la base de datos. "
                        f"Duplicados omitidos: {skipped_count}",
                    )
                else:
                    messages.error(
                        request,
                        f"No se pudieron cargar los datos. Errores: {error_count}",
                    )

                return redirect("csv_upload")

            except Exception as e:
                messages.error(request, f"Error al procesar el archivo CSV: {str(e)}")
                return redirect("csv_upload")
    else:
        form = CSVUploadForm()

    # Obtener estadísticas actuales del usuario
    stats = {
        "customers": Customers.objects.filter(user=request.user).count(),
        "products": Products.objects.filter(user=request.user).count(),
        "transactions": Transactions.objects.filter(user=request.user).count(),
        "categories": Categories.objects.count(),
        "locations": Locations.objects.count(),
    }

    context = {"form": form, "stats": stats}
    return render(request, "crud/csv_upload.html", context)


# ==================== DATA MANAGEMENT ====================


@login_required
def data_management(request):
    """Vista principal para gestión de datos"""
    stats = {
        "customers": Customers.objects.filter(user=request.user).count(),
        "products": Products.objects.filter(user=request.user).count(),
        "transactions": Transactions.objects.filter(user=request.user).count(),
        "categories": Categories.objects.count(),
        "payment_methods": PaymentMethods.objects.count(),
        "locations": Locations.objects.count(),
        "colors": Colors.objects.count(),
        "sizes": Sizes.objects.count(),
        "seasons": Seasons.objects.count(),
        "shipping_types": ShippingTypes.objects.count(),
    }

    context = {"stats": stats}
    return render(request, "crud/data_management.html", context)

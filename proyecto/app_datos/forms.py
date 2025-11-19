from django import forms
from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, NumberInput, Select, Textarea, TextInput

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


class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de la categoría"}
            )
        }


class PaymentMethodForm(ModelForm):
    class Meta:
        model = PaymentMethods
        fields = "__all__"
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del método de pago",
                }
            )
        }


class ShippingTypeForm(ModelForm):
    class Meta:
        model = ShippingTypes
        fields = "__all__"
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Tipo de envío"}
            )
        }


class PromotionForm(ModelForm):
    class Meta:
        model = Promotions
        fields = "__all__"
        widgets = {
            "promocode": TextInput(
                attrs={"class": "form-control", "placeholder": "Código promocional"}
            ),
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción de la promoción",
                    "rows": 3,
                }
            ),
        }


class LocationForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"
        widgets = {
            "state": TextInput(
                attrs={"class": "form-control", "placeholder": "Estado/Ubicación"}
            )
        }


class SizeForm(ModelForm):
    class Meta:
        model = Sizes
        fields = "__all__"
        widgets = {
            "size_label": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Talla (ej: S, M, L, XL)",
                }
            )
        }


class ColorForm(ModelForm):
    class Meta:
        model = Colors
        fields = "__all__"
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del color"}
            )
        }


class SeasonForm(ModelForm):
    class Meta:
        model = Seasons
        fields = "__all__"
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Temporada"}
            )
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        exclude = ["user"]
        widgets = {
            "age": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Edad",
                    "min": 1,
                    "max": 120,
                }
            ),
            "gender": TextInput(
                attrs={"class": "form-control", "placeholder": "Género (Male/Female)"}
            ),
            "id_location": Select(attrs={"class": "form-control"}),
            "sub_status": CheckboxInput(attrs={"class": "form-check-input"}),
            "id_paymentmethod": Select(attrs={"class": "form-control"}),
            "freq_purchase": TextInput(
                attrs={"class": "form-control", "placeholder": "Frecuencia de compra"}
            ),
            "prev_purchases": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Compras previas",
                    "min": 0,
                }
            ),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Products
        exclude = ["user"]
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del producto"}
            ),
            "id_category": Select(attrs={"class": "form-control"}),
            "id_size": Select(attrs={"class": "form-control"}),
            "id_color": Select(attrs={"class": "form-control"}),
            "id_season": Select(attrs={"class": "form-control"}),
        }


class TransactionForm(ModelForm):
    purchase_date = forms.DateField(
        widget=NumberInput(attrs={"type": "date", "class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Transactions
        exclude = ["user"]
        widgets = {
            "id_customer": Select(attrs={"class": "form-control"}),
            "id_product": Select(attrs={"class": "form-control"}),
            "purchase_amount": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Monto de compra",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "review_rate": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Calificación (0-5)",
                    "step": "0.1",
                    "min": "0",
                    "max": "5",
                }
            ),
            "id_paymentmethod": Select(attrs={"class": "form-control"}),
            "id_shipping": Select(attrs={"class": "form-control"}),
            "dsct_applied": CheckboxInput(attrs={"class": "form-check-input"}),
            "promo_used": CheckboxInput(attrs={"class": "form-check-input"}),
            "id_promotion": Select(attrs={"class": "form-control"}),
        }


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(
        label="Archivo CSV",
        help_text="Seleccione un archivo CSV para cargar",
        widget=forms.FileInput(attrs={"class": "form-control", "accept": ".csv"}),
    )

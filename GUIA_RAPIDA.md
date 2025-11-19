# 🚀 GUÍA RÁPIDA - CERTAMEN 2

## Inicio Rápido en 3 Pasos

### 1️⃣ Setup (Primera vez)
```bash
cd proyecto
./setup.sh          # Linux/Mac
# o
setup.bat           # Windows
```

### 2️⃣ Iniciar Servidor
```bash
python manage.py runserver
```

### 3️⃣ Acceder al Sistema
- **Dashboard:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

---

## 📋 Checklist de Requisitos

- [x] **1. Súper Usuario** → `python manage.py createsuperuser`
- [x] **2. Models.py** → 11 clases ORM en `app_datos/models.py`
- [x] **3. Admin.py** → 11 modelos registrados
- [x] **4. Makemigrations** → `python manage.py migrate`
- [x] **5. Formularios** → 12 formularios en `forms.py`
- [x] **6. Carga CSV** → URL: `/csv-upload/` con control de duplicados
- [x] **7. Messages/Toast/Modal** → Triple sistema implementado
- [x] **8. Sorpréndame** → 20+ innovaciones frontend/backend

---

## 🎯 Funciones Principales

### Gestión de Datos
| Función | URL | Descripción |
|---------|-----|-------------|
| Panel Principal | `/data/` | Vista de estadísticas |
| Cargar CSV | `/csv-upload/` | Importar datos masivos |
| Clientes | `/customers/` | CRUD completo |
| Productos | `/products/` | CRUD completo |
| Transacciones | `/transactions/` | CRUD completo |

### Visualizaciones (12 gráficos)
- Histogramas, Pie Charts, Bar Charts, Line Charts, Scatter Plots
- Todas las visualizaciones accesibles desde el menú lateral

---

## 🔥 Características Destacadas

### Control de Duplicados en CSV
✅ **Problema resuelto:** Si cargas el CSV 2+ veces, NO duplica datos
- Primera carga: Inserta todo
- Segunda carga: Detecta duplicados y los omite
- Muestra estadísticas: "Creados: X, Omitidos: Y"

### Triple Sistema de Notificaciones
1. **Django Messages** → Alertas persistentes (auto-cierre 5s)
2. **Bootstrap Toast** → Notificaciones emergentes
3. **SweetAlert2** → Confirmaciones modales elegantes

### UI Moderna
- 🎨 Animaciones suaves y efectos hover
- 📱 100% responsive (móvil, tablet, desktop)
- 🌈 Código de colores semántico
- ⚡ Feedback visual en todas las acciones

---

## 📝 Datos de Prueba

### Cargar Dataset Completo
1. Ir a http://127.0.0.1:8000/csv-upload/
2. Seleccionar `shopping_trends.csv`
3. Click "Iniciar Carga"
4. ✅ Ver estadísticas de importación

### Crear Registro Manual
1. Click "Agregar Cliente/Producto/Transacción"
2. Llenar formulario
3. Guardar
4. ✅ Ver mensaje de confirmación con SweetAlert2

---

## 🛠️ Comandos Útiles

```bash
# Ver migraciones pendientes
python manage.py showmigrations

# Crear nueva migración
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Shell de Django
python manage.py shell

# Verificar proyecto
python manage.py check
```

---

## 📂 Archivos Importantes

```
proyecto/
├── app_datos/
│   ├── models.py       ← 11 modelos ORM
│   ├── views.py        ← 30+ vistas
│   ├── forms.py        ← 12 formularios
│   ├── urls.py         ← 30+ rutas
│   └── templates/      ← 20+ templates
├── db.sqlite3          ← Base de datos
├── shopping_trends.csv ← Dataset CSV
└── manage.py
```

---

## 🎨 Innovaciones Implementadas

### Frontend
- ✨ Dashboard con estadísticas en tiempo real
- 🎭 Sidebar con gradientes y animaciones
- 🃏 Cards interactivas con efectos 3D
- 🌟 Badges de estado coloridos
- 🔔 Notificaciones tipo "toast"
- 💬 Modales de confirmación elegantes

### Backend
- 🧠 Control inteligente de duplicados
- 🔒 Transacciones atómicas
- ⚡ Queries optimizadas (select_related)
- ✅ Validación multinivel
- 🛡️ Manejo robusto de errores

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'django'"
→ Activar entorno virtual: `source ../mienv/bin/activate`

### "Table doesn't exist"
→ Aplicar migraciones: `python manage.py migrate`

### CSV no carga
→ Verificar nombre: `shopping_trends.csv` en carpeta `proyecto/`

### No veo datos en el dashboard
→ Primero cargar CSV o agregar datos manualmente

---

## 📊 Modelos del Sistema

1. **Categories** - Categorías de productos
2. **PaymentMethods** - Métodos de pago
3. **ShippingTypes** - Tipos de envío
4. **Promotions** - Códigos promocionales
5. **Locations** - Estados/Ubicaciones
6. **Sizes** - Tallas (S, M, L, XL)
7. **Colors** - Colores de productos
8. **Seasons** - Temporadas (Winter, Spring, Summer, Fall)
9. **Customers** - Clientes (tabla principal)
10. **Products** - Productos del catálogo
11. **Transactions** - Ventas/Compras

**Relaciones:** FK entre Customers↔Locations, Products↔Categories, Transactions↔Customers↔Products

---

## ✅ Verificación Rápida

```bash
# 1. Verificar modelos
python manage.py shell
>>> from app_datos.models import *
>>> Customers.objects.count()  # Debe retornar número

# 2. Verificar admin
# Ir a http://127.0.0.1:8000/admin/
# Login con superusuario
# Ver 11 modelos listados

# 3. Verificar formularios
# Ir a http://127.0.0.1:8000/customers/add/
# Ver formulario con validación

# 4. Verificar CSV
# Ir a http://127.0.0.1:8000/csv-upload/
# Cargar archivo
# Ver estadísticas
```

---

## 🎓 Para la Demostración

1. **Mostrar Dashboard** → Estadísticas en tiempo real
2. **Mostrar Carga CSV** → Control de duplicados
3. **Mostrar CRUD** → Agregar cliente con formulario
4. **Mostrar Notificaciones** → Messages, Toast, SweetAlert2
5. **Mostrar Gráficos** → Cualquiera de los 12
6. **Mostrar Innovación** → UI moderna, animaciones, responsive

---

## 📚 Documentación Completa

- **INSTRUCCIONES.md** → Manual completo de uso
- **RESUMEN_IMPLEMENTACION.md** → Detalles técnicos
- **GUIA_RAPIDA.md** → Este archivo

---

## 🏆 Puntos Clave para Evaluación

✅ **ORM:** 11 modelos con relaciones FK
✅ **Admin:** Todos registrados
✅ **Forms:** 12 formularios con validación
✅ **CSV:** Con control de duplicados (¡importante!)
✅ **Messages:** Django + Toast + SweetAlert2 (triple sistema)
✅ **Sorpresa:** UI moderna + optimizaciones backend

---

**¡Proyecto 100% funcional y listo para demostrar!** 🎉
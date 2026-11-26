# Sistema de Control de Inventario (inventario-app)

Estudiante: Rodrigo Xavier Maya Noriega
Tema asignado: Control de Inventario

## Descripcion de las cuatro tablas y sus relaciones

La aplicacion maneja el control de inventario de una bodega con 4 modelos separados en la carpeta `inventario/models/`:

1. **Categoria** (`categoria.py`): guarda el nombre de la categoria, codigo_pasillo, descripcion y si esta activa
2. **Proveedor** (`proveedor.py`): guarda los datos de los provedores como nombre, ruc, telefono, correo, ciudad y fecha_registro
3. **Producto** (`producto.py`): es la tabla principal del inventario, tiene codigo_sku, nombre, descripcion, precio_unitario (DecimalField), stock_actual, stock_minimo, estado (TextChoices) y fecha_ingreso
   - Tiene una ForeignKey hacia `Categoria` con `on_delete=models.PROTECT` y `related_name='productos'`
   - Tiene un ManyToManyField con `Proveedor` con `related_name='productos'`
   - Tiene una ForeignKey `creado_por` hacia `User` para que un consultor solo pueda editar los productos que el mismo creo
4. **Movimiento** (`movimiento.py`): registra entradas, salidas y ajustes de stock con tipo (TextChoices), cantidad, costo_unitario (DecimalField), fecha_movimiento y motivo
   - Tiene una ForeignKey hacia `Producto` con `on_delete=models.CASCADE` y `related_name='movimientos'`

```text
Categoria (1) -----> (N) Producto (N) <-----> (M) Proveedor
                            |
                           (1)
                            |
                            v
                           (N)
                        Movimiento
```

## Pasos para levantar el proyecto desde cero

1. Clonar el repositorio y entrar a la carpeta:
```bash
git clone https://github.com/rodrigomaya/inventario-app.git
cd inventario-app
```

2. Crear y activar el entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar las migraciones:
```bash
python manage.py migrate
```

5. Cargar los grupos, usuarios y datos de prueba (6 registros por tabla):
```bash
python manage.py cargar_datos
```

6. Iniciar el servidor:
```bash
python manage.py runserver
```

## Tabla de usuarios de prueba

| Usuario | Contrasena | Grupo / Rol | Permisos |
| :--- | :--- | :--- | :--- |
| `admin` | `Admin12345!` | Superusuario | Acceso total al admin y a las 4 tablas |
| `admin_inv` | `Admin12345!` | `administradores` | Puede crear, editar y eliminar en las 4 entidades |
| `consultor` | `Consultor12345!` | `consultores` | Puede ver listados y detalles, crear productos y editar solo los productos que el creo |
| `consultor2` | `Consultor12345!` | `consultores` | Otro usuario consultor para probar que no puede editar productos de otro usuario |

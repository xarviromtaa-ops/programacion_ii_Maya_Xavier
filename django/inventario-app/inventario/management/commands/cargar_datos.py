from datetime import date
from decimal import Decimal

from django.contrib.auth.models import Group, Permission, User
from django.core.management.base import BaseCommand

from inventario.models import Categoria, Movimiento, Producto, Proveedor


class Command(BaseCommand):
    help = 'Crea los grupos permisos usuarios de prueba y registros iniciales'

    def handle(self, *args, **options):
        grupo_admin, _ = Group.objects.get_or_create(name='administradores')
        permisos_admin = Permission.objects.filter(
            content_type__app_label='inventario'
        )
        grupo_admin.permissions.set(permisos_admin)

        grupo_consultores, _ = Group.objects.get_or_create(name='consultores')
        permisos_consultor = Permission.objects.filter(
            content_type__app_label='inventario',
            codename__in=[
                'view_categoria',
                'view_proveedor',
                'view_producto',
                'view_movimiento',
                'add_producto',
                'change_producto',
            ],
        )
        grupo_consultores.permissions.set(permisos_consultor)

        superuser, _ = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@correo.com', 'is_staff': True, 'is_superuser': True},
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.set_password('Admin12345!')
        superuser.save()

        user_admin, _ = User.objects.get_or_create(
            username='admin_inv',
            defaults={'email': 'admin_inv@correo.com'},
        )
        user_admin.set_password('Admin12345!')
        user_admin.save()
        user_admin.groups.set([grupo_admin])

        user_consultor, _ = User.objects.get_or_create(
            username='consultor',
            defaults={'email': 'consultor@correo.com'},
        )
        user_consultor.set_password('Consultor12345!')
        user_consultor.save()
        user_consultor.groups.set([grupo_consultores])

        user_consultor2, _ = User.objects.get_or_create(
            username='consultor2',
            defaults={'email': 'consultor2@correo.com'},
        )
        user_consultor2.set_password('Consultor12345!')
        user_consultor2.save()
        user_consultor2.groups.set([grupo_consultores])

        datos_categorias = [
            ('Equipos de Computo', 'PAS-A01', 'Laptops y equipos informaticos'),
            ('Redes y Conectividad', 'PAS-A02', 'Switches routers y cableado'),
            ('Herramientas Electricas', 'PAS-B01', 'Taladros y equipos de mantenimiento'),
            ('Seguridad Industrial', 'PAS-B02', 'Cascos guantes y gafas de proteccion'),
            ('Suministros de Oficina', 'PAS-C01', 'Papeleria carpetas y consumibles'),
            ('Componentes Electronicos', 'PAS-C02', 'Multimetros sensores y repuestos'),
        ]
        categorias = {}
        for nombre, pasillo, descripcion in datos_categorias:
            cat, _ = Categoria.objects.update_or_create(
                nombre=nombre,
                defaults={
                    'codigo_pasillo': pasillo,
                    'descripcion': descripcion,
                    'activa': True,
                },
            )
            categorias[nombre] = cat

        datos_proveedores = [
            ('TecnoGlobal SA', '1790012345001', '022456789', 'ventas@tecnoglobal.ec', 'Quito', date(2025, 1, 15)),
            ('Importadora Andina', '0991122334001', '042334455', 'contacto@andina.ec', 'Guayaquil', date(2025, 2, 10)),
            ('Ferreteria del Pacifico', '1792233445001', '072889900', 'pedidos@ferrepacifico.ec', 'Cuenca', date(2025, 3, 5)),
            ('Suministros Ecuador', '1793344556001', '022998877', 'info@sumicorp.ec', 'Quito', date(2025, 4, 12)),
            ('Redes del Sur', '0194455667001', '032556677', 'soporte@redessur.ec', 'Ambato', date(2025, 5, 20)),
            ('ElectroPartes SA', '1795566778001', '052667788', 'logistica@electropartes.ec', 'Manta', date(2025, 6, 18)),
        ]
        proveedores = {}
        for nombre, ruc, telefono, correo, ciudad, fecha_reg in datos_proveedores:
            prov, _ = Proveedor.objects.update_or_create(
                ruc=ruc,
                defaults={
                    'nombre': nombre,
                    'telefono': telefono,
                    'correo': correo,
                    'ciudad': ciudad,
                    'fecha_registro': fecha_reg,
                },
            )
            proveedores[ruc] = prov

        datos_productos = [
            ('SKU-COMP-001', 'Laptop Empresarial 14', 'Portatil Core i7 16GB RAM', categorias['Equipos de Computo'], Decimal('980.00'), 15, 5, Producto.EstadoProducto.DISPONIBLE, date(2026, 1, 10), user_admin, ['1790012345001', '0991122334001']),
            ('SKU-RED-002', 'Switch Gigabit 24 Puertos', 'Switch administrable de red', categorias['Redes y Conectividad'], Decimal('320.50'), 10, 3, Producto.EstadoProducto.DISPONIBLE, date(2026, 1, 18), user_admin, ['0194455667001']),
            ('SKU-HER-003', 'Taladro Inalambrico 20V', 'Taladro percutor con maletin', categorias['Herramientas Electricas'], Decimal('145.75'), 22, 5, Producto.EstadoProducto.DISPONIBLE, date(2026, 2, 4), user_consultor, ['1792233445001']),
            ('SKU-SEG-004', 'Casco Dielectrico Tipo I', 'Casco de seguridad industrial', categorias['Seguridad Industrial'], Decimal('18.90'), 4, 10, Producto.EstadoProducto.STOCK_BAJO, date(2026, 2, 12), user_consultor, ['1792233445001']),
            ('SKU-OFI-005', 'Caja Resmas Papel A4', 'Caja de 10 resmas de papel bond', categorias['Suministros de Oficina'], Decimal('42.00'), 60, 15, Producto.EstadoProducto.DISPONIBLE, date(2026, 2, 20), user_consultor2, ['1793344556001']),
            ('SKU-ELE-006', 'Multimetro Digital True RMS', 'Multimetro industrial CAT IV', categorias['Componentes Electronicos'], Decimal('89.99'), 8, 4, Producto.EstadoProducto.DISPONIBLE, date(2026, 3, 1), user_admin, ['1795566778001']),
        ]
        productos = {}
        for sku, nombre, desc, categoria, precio, stock, minimo, estado, fecha_ing, creador, rucs in datos_productos:
            prod, _ = Producto.objects.update_or_create(
                codigo_sku=sku,
                defaults={
                    'nombre': nombre,
                    'descripcion': desc,
                    'categoria': categoria,
                    'precio_unitario': precio,
                    'stock_actual': stock,
                    'stock_minimo': minimo,
                    'estado': estado,
                    'fecha_ingreso': fecha_ing,
                    'creado_por': creador,
                },
            )
            prod.proveedores.set([proveedores[r] for r in rucs])
            productos[sku] = prod

        datos_movimientos = [
            (productos['SKU-COMP-001'], Movimiento.TipoMovimiento.ENTRADA, 15, Decimal('910.00'), date(2026, 1, 11), 'Compra inicial de laptops', user_admin),
            (productos['SKU-RED-002'], Movimiento.TipoMovimiento.ENTRADA, 10, Decimal('290.00'), date(2026, 1, 19), 'Ingreso de switches para bodega', user_admin),
            (productos['SKU-HER-003'], Movimiento.TipoMovimiento.ENTRADA, 25, Decimal('125.00'), date(2026, 2, 5), 'Orden de compra 41', user_consultor),
            (productos['SKU-HER-003'], Movimiento.TipoMovimiento.SALIDA, 3, Decimal('145.75'), date(2026, 2, 14), 'Entrega a mantenimiento', user_admin),
            (productos['SKU-SEG-004'], Movimiento.TipoMovimiento.SALIDA, 16, Decimal('18.90'), date(2026, 2, 22), 'Dotacion de seguridad a tecnicos', user_admin),
            (productos['SKU-ELE-006'], Movimiento.TipoMovimiento.AJUSTE, 8, Decimal('82.00'), date(2026, 3, 3), 'Ajuste por inventario fisico', user_admin),
        ]
        for prod, tipo, cantidad, costo, fecha_mov, motivo, creador in datos_movimientos:
            Movimiento.objects.update_or_create(
                producto=prod,
                tipo=tipo,
                fecha_movimiento=fecha_mov,
                motivo=motivo,
                defaults={
                    'cantidad': cantidad,
                    'costo_unitario': costo,
                    'creado_por': creador,
                },
            )

        self.stdout.write(self.style.SUCCESS('Grupos usuarios y datos de prueba cargados correctamente'))

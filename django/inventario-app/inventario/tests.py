from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import TestCase
from django.urls import reverse

from inventario.models import Categoria, Producto


class ProductoPermissionTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.grupo_admin = Group.objects.create(name='administradores')
        self.grupo_Admin_perms = Permission.objects.filter(
            content_type__app_label='inventario'
        )
        self.grupo_admin.permissions.set(self.grupo_Admin_perms)

        self.grupo_consultores = Group.objects.create(name='consultores')
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
        self.grupo_consultores.permissions.set(permisos_consultor)

        self.admin_user = User.objects.create_user(
            username='admin_inv',
            password='test-password',
        )
        self.admin_user.groups.add(self.grupo_admin)

        self.consultor = User.objects.create_user(
            username='consultor',
            password='test-password',
        )
        self.consultor.groups.add(self.grupo_consultores)

        self.categoria = Categoria.objects.create(
            nombre='Equipos de Computo',
            codigo_pasillo='PAS-A01',
        )
        self.producto_propio = Producto.objects.create(
            codigo_sku='SKU-001',
            nombre='Laptop',
            categoria=self.categoria,
            precio_unitario=Decimal('800.00'),
            stock_actual=5,
            stock_minimo=2,
            fecha_ingreso=date(2026, 1, 10),
            creado_por=self.consultor,
        )
        self.producto_ajeno = Producto.objects.create(
            codigo_sku='SKU-002',
            nombre='Switch',
            categoria=self.categoria,
            precio_unitario=Decimal('250.00'),
            stock_actual=4,
            stock_minimo=1,
            fecha_ingreso=date(2026, 1, 12),
            creado_por=self.admin_user,
        )

    def test_anonymous_user_is_redirected_to_cuentas_login(self):
        response = self.client.get(reverse('producto_create'))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('producto_create')}",
            fetch_redirect_response=False,
        )

    def test_cuentas_root_redirects_to_login(self):
        response = self.client.get('/cuentas/', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request['PATH_INFO'], reverse('login'))

    def test_registered_user_can_log_in_and_see_home(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'consultor', 'password': 'test-password'},
        )

        self.assertRedirects(response, reverse('home'))
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sesion iniciada como')
        self.assertContains(response, 'consultor')

    def test_consultor_without_permission_gets_forbidden(self):
        self.client.force_login(self.consultor)

        response = self.client.get(reverse('categoria_create'))

        self.assertEqual(response.status_code, 403)

    def test_consultor_can_edit_own_producto_but_not_others(self):
        self.client.force_login(self.consultor)

        resp_propio = self.client.get(
            reverse('producto_update', kwargs={'pk': self.producto_propio.pk})
        )
        self.assertEqual(resp_propio.status_code, 200)

        resp_ajeno = self.client.get(
            reverse('producto_update', kwargs={'pk': self.producto_ajeno.pk})
        )
        self.assertEqual(resp_ajeno.status_code, 403)

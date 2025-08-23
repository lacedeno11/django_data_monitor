from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Crea usuarios con diferentes niveles de acceso'

    def handle(self, *args, **options):
        # 1. SUPERUSUARIO ADMIN (acceso total)
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@localhost.com',
                password='admin123',
                first_name='Super',
                last_name='Admin'
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superusuario creado: admin / admin123')
            )
        else:
            admin_user = User.objects.get(username='admin')
            self.stdout.write(
                self.style.WARNING('⚠️  Superusuario admin ya existe')
            )

        # 2. USUARIO DASHBOARD (acceso al dashboard)
        if not User.objects.filter(username='dashboard_user').exists():
            dashboard_user = User.objects.create_user(
                username='dashboard_user',
                email='dashboard@localhost.com',
                password='dashboard123',
                first_name='Dashboard',
                last_name='User',
                is_staff=True,  # Puede acceder al admin pero con permisos limitados
                is_active=True
            )
            
            # Crear grupo Dashboard si no existe
            dashboard_group, created = Group.objects.get_or_create(name='Dashboard Users')
            if created:
                # Agregar permisos básicos al grupo dashboard
                permissions = [
                    'auth.view_user',  # Ver usuarios
                    'auth.view_group',  # Ver grupos
                    # Puedes agregar más permisos según tus modelos
                ]
                for perm_codename in permissions:
                    try:
                        app_label, codename = perm_codename.split('.')
                        permission = Permission.objects.get(
                            content_type__app_label=app_label,
                            codename=codename
                        )
                        dashboard_group.permissions.add(permission)
                    except Permission.DoesNotExist:
                        pass
            
            dashboard_user.groups.add(dashboard_group)
            self.stdout.write(
                self.style.SUCCESS(f'✅ Usuario dashboard creado: dashboard_user / dashboard123')
            )
        else:
            self.stdout.write(
                self.style.WARNING('⚠️  Usuario dashboard_user ya existe')
            )

        # 3. USUARIO RESTRINGIDO (error 403)
        if not User.objects.filter(username='restricted_user').exists():
            restricted_user = User.objects.create_user(
                username='restricted_user',
                email='restricted@localhost.com',
                password='restricted123',
                first_name='Restricted',
                last_name='User',
                is_staff=False,  # NO puede acceder al admin
                is_active=True
            )
            
            # Crear grupo de usuarios restringidos
            restricted_group, created = Group.objects.get_or_create(name='Restricted Users')
            # Este grupo NO tendrá permisos, por lo que verá 403
            
            restricted_user.groups.add(restricted_group)
            self.stdout.write(
                self.style.SUCCESS(f'✅ Usuario restringido creado: restricted_user / restricted123')
            )
        else:
            self.stdout.write(
                self.style.WARNING('⚠️  Usuario restricted_user ya existe')
            )

        # Mostrar resumen
        self.stdout.write(
            self.style.SUCCESS('\n🎉 USUARIOS CREADOS:')
        )
        self.stdout.write('1. admin / admin123 - Superusuario (acceso total)')
        self.stdout.write('2. dashboard_user / dashboard123 - Usuario dashboard (acceso limitado)')
        self.stdout.write('3. restricted_user / restricted123 - Usuario restringido (error 403)')
        self.stdout.write('\n💡 Puedes usar estos usuarios para probar diferentes niveles de acceso')

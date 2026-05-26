# Generated manually for Sprint final - auditoría de usabilidad

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_historialguia_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('criterio', models.CharField(max_length=100)),
                ('accion', models.CharField(max_length=180)),
                ('resultado', models.CharField(choices=[('exitoso', 'Exitoso'), ('fallido', 'Fallido'), ('bloqueado', 'Bloqueado'), ('error', 'Error')], default='exitoso', max_length=20)),
                ('detalle', models.TextField(blank=True)),
                ('numero_guia', models.CharField(blank=True, max_length=200)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('metodo', models.CharField(blank=True, max_length=10)),
                ('ruta', models.CharField(blank=True, max_length=255)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
    ]

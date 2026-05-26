# Generated manually for Sprint final - hacer IP flexible para Render/Cloudflare

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auditoriausuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditoriausuario',
            name='ip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

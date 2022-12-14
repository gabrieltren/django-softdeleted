# Generated by Django 4.0.6 on 2022-08-10 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True, verbose_name='UUID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('deletado_em', models.DateTimeField(blank=True, null=True, verbose_name='Deletado em')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('texto', models.TextField(blank=True, null=True, verbose_name='Texto')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado_em'],
                'abstract': False,
            },
        ),
    ]

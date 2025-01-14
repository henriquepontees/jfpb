# Generated by Django 5.0.6 on 2024-05-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inovacaowebsite', '0002_album_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('assunto', models.CharField(max_length=100)),
                ('mensagem', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

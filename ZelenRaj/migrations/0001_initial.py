# Generated by Django 4.2.2 on 2023-06-21 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('delivery_address', models.CharField(max_length=200)),
                ('contact_information', models.CharField(max_length=100)),
                ('payment_method', models.BooleanField(choices=[(True, 'Електронско плаќање'), (False, 'Плаќање во готово при достава')])),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='plant_images/')),
                ('price', models.IntegerField()),
                ('care_info', models.TextField()),
                ('stock', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlantOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='ZelenRaj.order')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZelenRaj.plant')),
            ],
        ),
    ]

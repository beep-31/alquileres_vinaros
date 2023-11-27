# Generated by Django 4.2.5 on 2023-11-12 13:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_is_available_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSell',
            fields=[
                ('product_id', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('title_esp', models.CharField(default='Apartamento', max_length=100, verbose_name='Заголовок на испанком')),
                ('title_eng', models.CharField(default='Apartment', max_length=100, verbose_name='Заголовок на английском')),
                ('title_ru', models.CharField(default='Апартамент', max_length=100, verbose_name='Заголовок на русском')),
                ('title_uk', models.CharField(default='Апартаменти', max_length=100, verbose_name='Заголовок на украинском')),
                ('description_esp', models.TextField(default='', max_length=1000, verbose_name='Описание на испанком')),
                ('description_eng', models.TextField(default='', max_length=1000, verbose_name='Описание на английском')),
                ('description_ru', models.TextField(default='', max_length=1000, verbose_name='Описание на русском')),
                ('description_uk', models.TextField(default='', max_length=1000, verbose_name='Описание на украинском')),
                ('price', models.CharField(default='0', max_length=3, verbose_name='Цена')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('product_main_image', models.ImageField(default='', upload_to=main.models.ProductSell.get_folder_name, verbose_name='ГЛАВНОЕ ФОТО')),
                ('is_Available', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSellImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.models.ProductSellImage.get_folder_name, verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productsell')),
            ],
        ),
    ]
from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    def get_folder_name(self, filename):
        return f'images/{self.title_esp}/{filename}'
    product_id = models.CharField(max_length=3, primary_key=True, unique=True)
    title_esp = models.CharField(max_length=100, default='Apartamento', verbose_name='Заголовок на испанком')
    title_eng = models.CharField(max_length=100, default='Apartment', verbose_name='Заголовок на английском')
    title_ru = models.CharField(max_length=100, default='Апартамент', verbose_name='Заголовок на русском')
    title_uk = models.CharField(max_length=100, default='Апартаменти', verbose_name='Заголовок на украинском')
    max_person = models.CharField(max_length=2, default='1', verbose_name='Макс. человек')
    rooms_amount = models.CharField(max_length=3, default='1', verbose_name='Кол-во комнат')
    is_best_offer = models.BooleanField(default=False, verbose_name='Лучшее предложение')
    has_AirConditioner = models.BooleanField(default=False, verbose_name='Есть кондиционер')
    has_Beach = models.BooleanField(default=False, verbose_name='Есть пляж')
    summer_price = models.CharField(max_length=3, default='0', verbose_name='Цена летом')
    rest_of_year_price = models.CharField(max_length=5, default='0', verbose_name='Цена в остальное время года')
    description_esp = models.TextField(max_length=1000, default='', verbose_name='Описание на испанком')
    description_eng = models.TextField(max_length=1000, default='', verbose_name='Описание на английском')
    description_ru = models.TextField(max_length=1000, default='', verbose_name='Описание на русском')
    description_uk = models.TextField(max_length=1000, default='', verbose_name='Описание на украинском')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    product_main_image = models.ImageField(null=False, blank=False, upload_to = get_folder_name, default='', verbose_name='ГЛАВНОЕ ФОТО')
    is_Available = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __str__(self):
        return self.title_ru
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def get_folder_name(self, filename):
        return f'images/{self.product.title_esp}/{filename}'
    image = models.ImageField(upload_to=get_folder_name, verbose_name='Фото')
    def __str__(self):
        return self.product.title_ru
    
class ProductSell(models.Model):
    def get_folder_name(self, filename):
        return f'images/venta/{self.title_esp}/{filename}'
    product_id = models.CharField(max_length=3, primary_key=True, unique=True)
    title_esp = models.CharField(max_length=100, default='Apartamento', verbose_name='Заголовок на испанком')
    title_eng = models.CharField(max_length=100, default='Apartment', verbose_name='Заголовок на английском')
    title_ru = models.CharField(max_length=100, default='Апартамент', verbose_name='Заголовок на русском')
    title_uk = models.CharField(max_length=100, default='Апартаменти', verbose_name='Заголовок на украинском')
    description_esp = models.TextField(max_length=1000, default='', verbose_name='Описание на испанком')
    description_eng = models.TextField(max_length=1000, default='', verbose_name='Описание на английском')
    description_ru = models.TextField(max_length=1000, default='', verbose_name='Описание на русском')
    description_uk = models.TextField(max_length=1000, default='', verbose_name='Описание на украинском')
    rooms_amount = models.CharField(max_length=3, default='1', verbose_name='Кол-во комнат')
    price = models.CharField(max_length=10, default='0', verbose_name='Цена')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    product_main_image = models.ImageField(null=False, blank=False, upload_to = get_folder_name, default='', verbose_name='ГЛАВНОЕ ФОТО')
    has_AirConditioner = models.BooleanField(default=False, verbose_name='Есть кондиционер')
    has_Beach = models.BooleanField(default=False, verbose_name='Есть пляж')
    is_Available = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    def __str__(self):
        return self.title_ru

class ProductSellImage(models.Model):
    product = models.ForeignKey(ProductSell, on_delete=models.CASCADE)
    def get_folder_name(self, filename):
        return f'images/venta/{self.product.title_esp}/{filename}'
    image = models.ImageField(upload_to=get_folder_name, verbose_name='Фото')
    def __str__(self):
        return self.product.title_ru

class UserContact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    message = models.TextField(verbose_name='Сообщение')
    submission_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    def __str__(self):
        return self.email

class Availability(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_data = models.DateField()
    end_data = models.DateField()
    

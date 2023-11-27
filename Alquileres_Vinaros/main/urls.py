from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


APP_NAME = 'main'

urlpatterns = [
    path("", views.homepage_esp, name='homepage_esp'),
    path("eng", views.homepage_eng, name='homepage_eng'),
    path("ru", views.homepage_ru, name='homepage_ru'),
    path("uk", views.homepage_uk, name='homepage_uk'),
    path("catalog", views.catalog_esp, name='catalog_esp'),
    path("eng/catalog", views.catalog_eng, name='catalog_eng'),
    path("ru/catalog", views.catalog_ru, name='catalog_ru'),
    path("uk/catalog", views.catalog_uk, name='catalog_uk'),
    path("catalog/<int:product_id>/", views.product_detail_esp, name='product_detail_esp'),
    path("eng/catalog/<int:product_id>/", views.product_detail_eng, name='product_detail_eng'),
    path("ru/catalog/<int:product_id>/", views.product_detail_ru, name='product_detail_ru'),
    path("uk/catalog/<int:product_id>/", views.product_detail_uk, name='product_detail_uk'),
    path("eng/about", views.about_eng, name="about-eng"),
    path("about", views.about_esp, name='about_esp'),
    path("ru/about", views.about_ru, name='about_ru'),
    path("uk/about", views.about_uk, name='about_uk'),
    path("eng/sales", views.sales_eng, name='sales_eng'),
    path("eng/sales/<int:product_id>/", views.detail_sales_eng, name='detail_sales_eng'),
    path("sales", views.sales_es, name='sales_eng'),
    path("sales/<int:product_id>/", views.detail_sales_es, name='detail_sales_es'),
    path("ru/sales", views.sales_ru, name='sales_ru'),
    path("ru/sales/<int:product_id>/", views.detail_sales_ru, name='detail_sales_ru'),
    path("uk/sales", views.sales_uk, name='sales_uk'),
    path("uk/sales/<int:product_id>/", views.detail_sales_uk, name='detail_sales_uk')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
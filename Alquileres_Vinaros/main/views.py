from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage, UserContact, Availability, ProductSell, ProductSellImage
from django.core.mail import EmailMessage
import datetime


def contact(request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['textarea']
        title = request.POST['title']
            # send_email = EmailMessage(
            #     name,
            #     title,
            #     message,
            #     email,
            #     ['your@email.com'],
            #     reply_to=[email],
            # )
            # send_email.send()
        userContact = UserContact(
            name = name,
            email = email,
            title = title,
            message = message,
        )

        userContact.save()

def search_products(start, finish):
    products = Product.objects.all()
    product_sorted_list = []
    for product in products:
        availability = Availability.objects.filter(product = product)
        if not availability:
            pass
        else:
            formated_start_time = availability[0].start_data.strftime("%Y-%m-%D")
            formated_finish_time = availability[0].end_data.strftime("%Y-%m-%D")
            if start >= formated_start_time and finish <= formated_finish_time:
                product_sorted_list.append(product)
    return product_sorted_list

# Create your views here.
def homepage_esp(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    return render(request,
                  'main/index.html',
                  {'products' : products})

def homepage_eng(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    return render(request=request,
                  template_name="main/index-eng.html",
                  context={"products":products})

def homepage_ru(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    return render(request=request,
                  template_name="main/index-ru.html",
                  context={"products":products})

def homepage_uk(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    for item in products:
        print(item.product_main_image.url)
    return render(request=request,
                  template_name="main/index-uk.html",
                  context={"products":products})

def catalog_esp(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    todays_date = datetime.date.today()
    year = str(todays_date.year)
    month = str(todays_date.month)
    day = str(todays_date.day)
    if(len(day)==1):
        day = "0" + day
    if(len(month) == 1):
        month = "0" + month
    start = request.GET.get('check-in', None)
    finish = request.GET.get('check-out', None)
    if start != None and finish != None:
        product_sorted_list = search_products(start, finish)
        return render(request=request, template_name="catalog/catalog-es.html", context={"products": product_sorted_list, "year": year, "month": month, "day": day, "start": start, "finish": finish})
    return render(request=request,
                  template_name="catalog/catalog-es.html",
                  context={"products":products, "year": year, "month": month, "day": day})

def catalog_eng(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    todays_date = datetime.date.today()
    year = str(todays_date.year)
    month = str(todays_date.month)
    day = str(todays_date.day)
    if(len(day)==1):
        day = "0" + day
    if(len(month) == 1):
        month = "0" + month
    start = request.GET.get('check-in', None)
    finish = request.GET.get('check-out', None)
    if start != None and finish != None:
        product_sorted_list = search_products(start, finish)
        return render(request=request, template_name="catalog/catalog-eng.html", context={"products": product_sorted_list, "year": year, "month": month, "day": day, "start": start, "finish": finish})
    return render(request=request,
                  template_name="catalog/catalog-eng.html",
                  context={"products": products, "year": year, "month": month, "day": day})

def catalog_ru(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    todays_date = datetime.date.today()
    year = str(todays_date.year)
    month = str(todays_date.month)
    day = str(todays_date.day)
    if(len(day)==1):
        day = "0" + day
    if(len(month) == 1):
        month = "0" + month
    start = request.GET.get('check-in', None)
    finish = request.GET.get('check-out', None)
    if start != None and finish != None:
        product_sorted_list = search_products(start, finish)
        return render(request=request, template_name="catalog/catalog-ru.html", context={"products": product_sorted_list, "year": year, "month": month, "day": day, "start": start, "finish": finish})
    return render(request=request,
                  template_name="catalog/catalog-ru.html",
                  context={"products":products, "year": year, "month": month, "day": day})

def catalog_uk(request):
    if request.method == 'POST':
        contact(request)
    products = Product.objects.all()
    todays_date = datetime.date.today()
    year = str(todays_date.year)
    month = str(todays_date.month)
    day = str(todays_date.day)
    if(len(day)==1):
        day = "0" + day
    if(len(month) == 1):
        month = "0" + month
    start = request.GET.get('check-in', None)
    finish = request.GET.get('check-out', None)
    if start != None and finish != None:
        product_sorted_list = search_products(start, finish)
        return render(request=request, template_name="catalog/catalog-uk.html", context={"products": product_sorted_list, "year": year, "month": month, "day": day, "start": start, "finish": finish})
    return render(request=request,
                  template_name="catalog/catalog-uk.html",
                  context={"products":products, "year": year, "month": month, "day": day})

def product_detail_esp(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product = product)
    availability = Availability.objects.filter(product = product)
    return render(request=request,
                  template_name="detail_page/detail.html",
                  context={"product": product, "images": images, "availability": availability})

def product_detail_eng(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product = product)
    availability = Availability.objects.filter(product = product)
    return render(request=request,
                  template_name="detail_page/detail-eng.html",
                  context={"product": product, "images": images, "availability": availability})

def product_detail_ru(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product = product)
    availability = Availability.objects.filter(product = product)
    return render(request=request,
                  template_name="detail_page/detail-ru.html",
                  context={"product": product, "images": images, "availability": availability})

def product_detail_uk(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product = product)
    availability = Availability.objects.filter(product = product)
    return render(request=request,
                  template_name="detail_page/detail-uk.html",
                  context={"product": product, "images": images, "availability": availability})

def about_eng(request):
    if request.method == 'POST':
        contact(request)
    return render(request=request,
                  template_name="about/about-eng.html")

def about_esp(request):
    if request.method == 'POST':
        contact(request)
    return render(request=request,
                  template_name="about/about-esp.html")

def about_ru(request):
    if request.method == 'POST':
        contact(request)
    return render(request=request,
                  template_name="about/about-ru.html")

def about_uk(request):
    if request.method == 'POST':
        contact(request)
    return render(request=request,
                  template_name="about/about-uk.html")

def sales_eng(request):
    if request.method == 'POST':
        contact(request)
    products = ProductSell.objects.all()
    products_sorted = []
    for product in products:
        if product.is_Available:
            products_sorted.append(product)
    return render(request=request, template_name="sales/sales-eng.html", context = {"products": products_sorted})

def detail_sales_eng(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(ProductSell, pk = product_id)
    images = ProductSellImage.objects.filter(product = product)
    return render(request=request, template_name="sales_detail/eng.html", context={"product": product, "images": images})    

def sales_es(request):
    if request.method == 'POST':
        contact(request)
    products = ProductSell.objects.all()
    products_sorted = []
    for product in products:
        if product.is_Available:
            products_sorted.append(product)
    return render(request=request, template_name="sales/sales.html", context={"products": products_sorted})

def detail_sales_es(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(ProductSell, pk = product_id)
    images = ProductSellImage.objects.filter(product = product)
    return render(request=request, template_name="sales_detail/es.html", context={"product": product, "images": images})    

def sales_ru(request):
    if request.method == 'POST':
        contact(request)
    products = ProductSell.objects.all()
    products_sorted = []
    for product in products:
        if product.is_Available:
            products_sorted.append(product)
    return render(request=request, template_name="sales/sales-ru.html", context={"products": products_sorted})

def detail_sales_ru(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(ProductSell, pk = product_id)
    images = ProductSellImage.objects.filter(product = product)
    return render(request=request, template_name="sales_detail/ru.html", context={"product": product, "images": images}) 

def sales_uk(request):
    if request.method == 'POST':
        contact(request)
    products = ProductSell.objects.all()
    products_sorted = []
    for product in products:
        if product.is_Available:
            products_sorted.append(product)
    return render(request=request, template_name="sales/sales-uk.html", context={"products": products_sorted})

def detail_sales_uk(request, product_id):
    if request.method == 'POST':
        contact(request)
    product = get_object_or_404(ProductSell, pk = product_id)
    images = ProductSellImage.objects.filter(product = product)
    return render(request=request, template_name="sales_detail/uk.html", context={"product": product, "images": images})    
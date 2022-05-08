from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_flag = request.GET.get('sort', '')
    template = 'catalog.html'

    if sort_flag == '':
        phones = Phone.objects.all()

    elif sort_flag == 'name':
        phones = Phone.objects.all().order_by('name')

    elif sort_flag == 'min_price':
        phones = Phone.objects.all().order_by('price')

    elif sort_flag == 'max_price':
        phones = Phone.objects.all().order_by('-price')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)

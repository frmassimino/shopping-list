from django.shortcuts import render
from numpy.core.fromnumeric import prod
from .models import Buy, Category, MeasureUnit, Product
from datetime import date

# Create your views here.

def indexView(request):
    context = {

    }
    return render(request, 'forecast/index.html', context)

def buyView(request):
    if request.method == 'POST':
        new_buy = Buy(
            product=Product.objects.get(description=request.POST.get('product')),
            price=request.POST.get('price'),
            qty=request.POST.get('quantity'),
            buy_datetime=request.POST.get('date')
        )
        new_buy.save()

    context = {
        'category_list': Category.objects.all(),
        'product_list': Product.objects.all(),
        'measure_list': MeasureUnit.objects.all(),
        'buy_list': Buy.objects.all()
    }
    return render(request, 'forecast/buy.html', context)

def forecastView(request):
    product_list = set(Buy.objects.all().values_list('product__id', 'product__description'))
    forecast_list = []
    print(product_list)
    for product in product_list:
        x = 0
        day_list = []
        day_list_new = []
        filtered_list = Buy.objects.filter(product__id=product[0])
        if len(filtered_list) > 1: 
            for filteredBuy in filtered_list:
                day_list.append([filteredBuy.buy_datetime, filteredBuy.qty])
            day_list.sort()
            for x in range(0, len(day_list)-1,1):
                day_list_new.append((day_list[x+1][0] - day_list[x][0]).days/day_list[x][1])
            new_forecast = {
                'name':product[1], 
                'avg_days': round(sum(day_list_new)/len(day_list_new),1),
            }
            new_forecast['days_til_next_buy'] = new_forecast['avg_days'] - (date.today() - day_list[-1][0]).days
            forecast_list.append(new_forecast)
    print(forecast_list)
    context = {
        'forecast_list': forecast_list
    }
    return render(request, 'forecast/forecast.html', context)
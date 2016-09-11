import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.settings import DATE_FILTERS
from server.models import Stock


@csrf_exempt
def get_all_raw_data(request):
    date_range, stock = __get_date_range_and_stock_from_request(request)
    result = Stock.objects.filter(stock__in=stock)
    if date_range is not None and date_range is not "MAX":
        result = result.filter(date__range=DATE_FILTERS[date_range])
    return HttpResponse(json.dumps(list(result.values()), cls=DjangoJSONEncoder));


@csrf_exempt
def get_month_on_month_growth(request):
    date_range, stock = __get_date_range_and_stock_from_request(request)
    return HttpResponse("Month on month growth data recieved")


@csrf_exempt
def get_quarter_on_quarter_growth(request):
    date_range, stock = __get_date_range_and_stock_from_request(request)
    return HttpResponse("Quater on quater growth data recieved")


@csrf_exempt
def get_year_on_year_growth(request):
    date_range, stock = __get_date_range_and_stock_from_request(request)
    return HttpResponse("Year on year growth data recieved")


@csrf_exempt
def get_cumulative_table_data(request):
    date_range, stock = __get_date_range_and_stock_from_request(request)
    return HttpResponse("Cumulative table data recieved")


def __get_date_range_and_stock_from_request(request):
    date_range = request.POST.get('dateRange')
    stock = request.POST.get('stock')
    return date_range, stock

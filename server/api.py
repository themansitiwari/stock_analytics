import json
import ast
import datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Avg
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
    return HttpResponse(json.dumps(list(result.values()), cls=DjangoJSONEncoder))


@csrf_exempt
def get_month_on_month_growth(request):
    # Assuming that we will show MOM only for one specific month at a time
    # User will select the month and the year for which he wants to see MOM
    # UI will pass that data as {"year":YYYY, "month": MM}
    # Extract the Year and the month, get the average for that
    # Then get the average for previous month
    # Calculate MOM and send
    date_range, stock = __get_date_range_and_stock_from_request(request)
    date_range_dict = ast.literal_eval(date_range)
    today = datetime.date.today()
    succeding_month_date = today.replace(year=date_range_dict['year'], month=date_range_dict['month'])
    preceding_month_date = succeding_month_date - datetime.timedelta(days=1 * 365 / 12)
    average_succeding_month = Stock.objects.filter(stock=stock).filter(date__year=succeding_month_date.year).filter(date__month=succeding_month_date.month).aggregate(avg=Avg('close'))['avg']
    average_preceding_month = Stock.objects.filter(stock=stock).filter(date__year=preceding_month_date.year).filter(date__month=preceding_month_date.month).aggregate(avg=Avg('close'))['avg']
    result = (average_succeding_month-average_preceding_month)/average_preceding_month * 100
    return HttpResponse(result)


@csrf_exempt
def get_quarter_on_quarter_growth(request):
    # UI passes the data as {"year":YYYY, "quarter": "QX"}
    date_range, stock = __get_date_range_and_stock_from_request(request)
    date_range_dict = ast.literal_eval(date_range)
    quarter_mapping = {"Q1": 1,
                       "Q2": 4,
                       "Q3": 7,
                       "Q4": 10}
    today = datetime.date.today()
    print type(date_range_dict['quarter'])
    succeding_quarter_start_date = today.replace(year=date_range_dict['year'], month=quarter_mapping[date_range_dict['quarter']], day=1)
    if date_range_dict['quarter'] == "Q4":
        succeding_quarter_end_date = succeding_quarter_start_date.replace(month=12, day=31)
    else:
        succeding_quarter_end_date = succeding_quarter_start_date.replace(month=quarter_mapping[date_range_dict['quarter']]+3) - datetime.timedelta(days=1)
    preceding_quarter_end_date = succeding_quarter_start_date - datetime.timedelta(days=1)
    preceding_quarter_start_date = preceding_quarter_end_date.replace(month=preceding_quarter_end_date.month-2, day=1)
    succeding_date_range = [str(succeding_quarter_start_date), str(succeding_quarter_end_date)]
    preceding_date_range = [str(preceding_quarter_start_date), str(preceding_quarter_end_date)]
    average_succeding_quarter = Stock.objects.filter(stock=stock).filter(date__range=succeding_date_range).aggregate(avg=Avg('close'))['avg']
    average_preceding_quarter = Stock.objects.filter(stock=stock).filter(date__range=preceding_date_range).aggregate(avg=Avg('close'))['avg']
    result = (average_succeding_quarter-average_preceding_quarter) / average_preceding_quarter * 100
    return HttpResponse(result)


@csrf_exempt
def get_year_on_year_growth(request):
    # Just pass the year as data, YYYY
    date_range, stock = __get_date_range_and_stock_from_request(request)
    average_succeding_year = Stock.objects.filter(stock=stock).filter(date__year=date_range).aggregate(avg=Avg('close'))['avg']
    average_preceding_year = Stock.objects.filter(stock=stock).filter(date__year=date_range-1).aggregate(avg=Avg('close'))['avg']
    result = (average_succeding_year - average_preceding_year) / average_preceding_year * 100
    return HttpResponse(result)

@csrf_exempt
def get_cumulative_table_data(request):
    date_range, stocks = __get_date_range_and_stock_from_request(request)
    cumulative_data = {}
    stock_list = ast.literal_eval(stocks)
    for stock in stock_list:
        highest_high = Stock.objects.filter(stock=stock).order_by('-high').first()
        lowest_low = Stock.objects.filter(stock=stock).order_by('low').first()
        cumulative_data[str(stock)] = {}
        cumulative_data[str(stock)]['high'] = {}
        cumulative_data[str(stock)]['low'] = {}
        cumulative_data[str(stock)]['high']['value'] = highest_high.high
        cumulative_data[str(stock)]['high']['date'] = highest_high.date
        cumulative_data[str(stock)]['low']['value'] = lowest_low.low
        cumulative_data[str(stock)]['low']['date'] = lowest_low.date
    return HttpResponse(json.dumps(cumulative_data, cls=DjangoJSONEncoder))


def __get_date_range_and_stock_from_request(request):
    date_range = request.body('dateRange')
    stock = request.body('stock')
    return date_range, stock

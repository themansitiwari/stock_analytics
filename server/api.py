from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getAllRawData(request):
    date_range, stock = __getDateRangeAndStockFromRequest(request)
    return HttpResponse("All data received");

@csrf_exempt
def getMonthOnMothGrowth(request):
    date_range, stock = __getDateRangeAndStockFromRequest(request)
    return HttpResponse("Month on month growth data recieved")

@csrf_exempt
def getQuaterOnQuaterGrowth(request):
    date_range, stock = __getDateRangeAndStockFromRequest(request)
    return HttpResponse("Quater on quater growth data recieved")

@csrf_exempt
def getYearOnYearGrowth(request):
    date_range, stock = __getDateRangeAndStockFromRequest(request)
    return HttpResponse("Year on year growth data recieved")

@csrf_exempt
def getCumulativeTableData(request):
    date_range, stock = __getDateRangeAndStockFromRequest(request)
    return HttpResponse("Cumulative table data recieved")

def __getDateRangeAndStockFromRequest(request):
    date_range = request.POST.get('dateRange')
    stock = request.POST.get('stock')
    return date_range, stock
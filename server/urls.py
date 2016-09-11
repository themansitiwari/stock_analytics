from django.conf.urls import patterns, url

from server.views import IndexView, stockDashboard
from server.api import get_all_raw_data, get_month_on_month_growth, get_quarter_on_quarter_growth, get_year_on_year_growth, get_cumulative_table_data
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url('^$', IndexView.as_view(), name='index'),
    url('^dashboard$', stockDashboard, name='stockDashboard'),
    url(r'^api/getRawData$', get_all_raw_data, name='rawData'),
    url(r'^api/getMom$', get_month_on_month_growth, name='MonthOnMonth'),
    url(r'^api/getQoq$', get_quarter_on_quarter_growth, name='QuaterOnQuater'),
    url(r'^api/getYoy$', get_year_on_year_growth, name='YearOnYear'),
    url(r'^api/getCumulativeTable$', get_cumulative_table_data, name='CumulativeTable'),
    url(r'^admin/', admin.site.urls),
)

from django.conf.urls import patterns, url

from server.views import IndexView
from server.api import getAllRawData, getMonthOnMothGrowth, getQuaterOnQuaterGrowth, getYearOnYearGrowth, getCumulativeTableData
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url('^$', IndexView.as_view(), name='index'),
    url(r'^api/getRawData$', getAllRawData, name='rawData'),
    url(r'^api/getMom$', getMonthOnMothGrowth, name='MonthOnMonth'),
    url(r'^api/getQoq$', getQuaterOnQuaterGrowth, name='QuaterOnQuater'),
    url(r'^api/getYoy$', getYearOnYearGrowth, name='YearOnYear'),
    url(r'^api/getCumulativeTable$', getCumulativeTableData, name='CumulativeTable'),
    url(r'^admin/', admin.site.urls),
)

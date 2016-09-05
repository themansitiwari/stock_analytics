from django.conf.urls import patterns, url

from server.views import IndexView
from server.api import getAllRawData, getMonthOnMothGrowth, getQuaterOnQuaterGrowth, getYearOnYearGrowth, getCumulativeTableData

urlpatterns = patterns(
    '',

    url('^index/$', IndexView.as_view(), name='index'),
    url(r'^api/getRawData$', getAllRawData, name='rawData'),
    url(r'^api/getMom$', getAllRawData, name='MonthOnMonth'),
    url(r'^api/getQoq$', getAllRawData, name='QuaterOnQuater'),
    url(r'^api/getYoy$', getAllRawData, name='YearOnYear'),
    url(r'^api/getCumulativeTable$', getAllRawData, name='CumulativeTable'),
)

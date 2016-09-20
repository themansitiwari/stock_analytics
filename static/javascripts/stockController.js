'use strict';

stockAnalytics
  .controller("StockController", function ($scope, appService) {
  $scope.testVar = "Controller Success";
  $scope.filterObj = {"selectedStocks": "", "selectedDateRange": ""};
  $scope.dateRangeOptions = ["1W", "2W", "3W", "1M", "3M", "6M", "9M", "1Y", "3Y", "5Y", "MAX"];
  $scope.stockOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  $scope.formattedData = {};
  var seriesData = [];
  $scope.chartOptions = {"load": false};

  $scope.generateChart = function () {
    var postData = {
      "stock": $scope.filterObj.selectedStocks,
      "dateRange": $scope.filterObj.selectedDateRange
    };
    generateStockOverviewChart(postData);
  };

  var formatDataForMulSeries = function (data, categoryKey, seriesKey, seriesValueKey, keysToIgnore) {
    var chartData = {"categories": []}
    var dataLength = data.length;
    var tempSeries = {}, tempSeriesVal;
    for (var i = 0; i < dataLength; i++) {
      tempSeries = {};
      if (chartData.categories.indexOf(data[i][categoryKey]) === -1) {
        chartData.categories.push(data[i][categoryKey]);
      }

      tempSeriesVal = data[i][seriesValueKey] || 0;
      if (!chartData.hasOwnProperty(data[i][seriesKey])) {
        chartData[data[i][seriesKey]] = {"name": seriesKey + "-" +data[i][seriesKey], "data": []}
      }
      angular.forEach(data[i], function (val, key) {
        if (keysToIgnore.indexOf(key) === -1) {
          tempSeries[key] = val;
        }
      });

      chartData[data[i][seriesKey]].data.push({"y": tempSeriesVal, "myData": tempSeries});
    }
    return chartData;
  };

  var generateStockOverviewChart = function (postData) {
    appService.postData({"url": "/api/getRawData",
                        "method": "POST",
                        "data":  postData
    }).then(function (data) {
      $scope.formattedData = formatDataForMulSeries(data, "date", "stock", "close", ["id"])
      console.log($scope.formattedData);
      seriesData = [];
      angular.forEach($scope.formattedData, function(val, key) {
        if (key !== "categories") {
          seriesData.push(val);
        }
      });
      $scope.chartOptions = {
        title: {
          text: 'Stocks overview (Date vs Closing price)'
        },
        tooltip: {
          formatter: function() {
            var str = "";
            $.each(this.point.myData, function(i, s) {
              str += i + ' : ' + s + '<br>'
            });
            return str;
          }
        },
        xAxis: {
          categories: $scope.formattedData.categories
        },
        plotOptions: {
         line: {
           turboThreshold: $scope.formattedData.categories.length + 1
         }
        },
        yAxis: {
          title: {
              text: 'Closed Price'
          },
          plotLines: [{
              value: 0,
              width: 1,
              color: '#808080'
          }]
        },
        series: seriesData,
        load: true
      }
    });
  };
  
});

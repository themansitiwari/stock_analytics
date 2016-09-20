'use strict';

stockAnalytics.directive('hcChart', function () {
  return {
    restrict: 'A',
    scope: {
      options: '=',
      chartId: '@'
    },
    controller: function ($scope, $element) {
      $scope.$watch('options', function (newVal, oldVal) {
        $("#"+$scope.chartId).highcharts(newVal);
      }, true);
    }
  };
});

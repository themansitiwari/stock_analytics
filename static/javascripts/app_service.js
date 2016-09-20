stockAnalytics
  .service('appService', ['$http', '$q', function ($http, $q) {
  "use strict";

  this.getData = function (cfg) {
    var d = $q.defer();
    var url = cfg.url;
    var self = this;
    $http({
      url: cfg.url,
      method: cfg.method
    }).success(function (data) {
      d.resolve(data);
    }).error(function (error) {
      d.reject(error);
    });
    return d.promise;
  };
  
  this.postData = function (cfg) {
    var d = $q.defer(),
      self = this;
    console.log(cfg);
    $http({
      url: cfg.url,
      method: cfg.method,
      data: cfg.data,
      headers: {'Content-Type': 'application/json'}
    }).success(function (data) {
      console.log("Saved");
      d.resolve(data);
    }).error(function (error) {
      d.reject(error);
    });
    return d.promise;
  };

}]);

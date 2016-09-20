'use strict';

/**
 * Main module of the application. configuring routing here
 */
var stockAnalytics = angular
    .module('stockAnalytics', [
      'ngRoute',
      'ui.multiselect'
    ]);

stockAnalytics.config(function($interpolateProvider, $routeProvider, $locationProvider) {
    "use strict";

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    });
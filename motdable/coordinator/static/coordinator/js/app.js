'use strict';

/* App Module */


var app = angular.module('coordinator', ['coordinator.services', 'coordinator.directives']).
	config(['$routeProvider', function($routeProvider) {
		$routeProvider.
			when('/motdable', {templateUrl: BASE_URL + 'partials/main.html', controller: MainCtrl}).
			otherwise({redirectTo: '/motdable'});
	}]);
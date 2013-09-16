'use strict';

/* Services */

angular.module('ApiService', ['ngResource'])
	.factory('PlayCalls', function($resource){
		return $resource('/api/playcalls/.json');
	})
	.factory('Players', function($resource){
		return $resource('/api/players/.json');
	});
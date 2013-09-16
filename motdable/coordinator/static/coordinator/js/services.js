'use strict';

/* Services */

angular.module('coordinator.services', ['ngResource'])
	.value('version', '0.1')
	.factory('PlayCalls', function($resource){
		return $resource('/api/playcalls/.json');
	})
	.factory('Players', function($resource){
		return $resource('/api/players/.json');
	});
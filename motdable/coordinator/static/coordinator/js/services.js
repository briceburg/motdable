'use strict';

/* Services */

angular.module('coordinator.services', ['ngResource'])
	.value('version', '0.1')
	.factory('Playbooks', function($resource){
		return $resource('/api/playbooks/.json');
	})
	.factory('Hosts', function($resource){
		return $resource('/api/hosts/.json');
	})
	.factory('ExecutePlay', function($http){
		return {
			get: function(params){
				return $http.get('/coordinator/execute/',{
					params: params
				});
			}
		};
	});
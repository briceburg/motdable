'use strict';

/* Controllers */

function MainCtrl($scope, Hosts, Playbooks, ExecutePlay) {
	// populate host list from django rest-framework
	Hosts.query(function(data){
		$scope.hosts = data;
		$scope.selectedHost = null;
	});
	
	// populate playbook list from django rest-framework
	Playbooks.query(function(data){
		$scope.playbooks = data;
		$scope.selectedPlaybook = null;
	});
	
	// multimethod for toggling selection of current host/playbook
	$scope.selectItem = function(id, type, variables){
		var property = 'selected' + type;
		$scope[property] = ($scope[property] == id) ? null : id;
		
		$scope.canExecute = ($scope.selectedHost && $scope.selectedPlaybook);
		
        if(type == 'Playbook')
        {
        	$scope.variables = [];
        	
        	if($scope[property])
        	{
	        	angular.forEach(variables, function(value, key){
	        		this.push({name: value, supplied_value: ''});
	        	}, $scope.variables);
        	}
        }
	}
	
	// method for executing a playbook against a host
	$scope.execute = function(){
		if(!$scope.canExecute) return alert('Please select a Host and Playbook first.');
		if($scope.isExecuting) return;
		
		$scope.isExecuting = true;
		
		var outputFunc = function(response) {
			$scope.isExecuting = false;
			$scope.playbookOutput = (response.data.output) ? 
					response.data.output : response.data;
		};
		
		// prepare variables, we cannot use ng-repeat (key, value) + ng-model
		//  which would be more efficient: see http://jsfiddle.net/sirhc/z9cGm/
		var variables = {};
		angular.forEach($scope.variables, function(obj, key){
    		this[obj.name] = obj.supplied_value;
    	}, variables);
		
		
		ExecutePlay.get({
			hostId:		$scope.selectedHost,
			playbookId:	$scope.selectedPlaybook,
			variables:	variables
		})
		// promise.then(successCallback, errorCallback)
		.then(outputFunc, outputFunc);
		
	}
}

'use strict';

/* Controllers */

function MainCtrl($scope, Players, PlayCalls, ExecutePlay) {
	// populate player list from django rest-framework
	Players.query(function(data){
		$scope.players = data;
		$scope.selectedPlayer = null;
	});
	
	// populate playcall list from django rest-framework
	PlayCalls.query(function(data){
		$scope.playcalls = data;
		$scope.selectedPlayCall = null;
	});
	
	// multimethod for toggling selection of current player/playcall
	$scope.selectItem = function(id, type, options){
		var property = 'selected' + type;
		$scope[property] = ($scope[property] == id) ? null : id;
		
		$scope.canExecute = ($scope.selectedPlayer && $scope.selectedPlayCall);
		
        if(type == 'PlayCall')
        {
        	$scope.options = [];
        	
        	if($scope[property])
        	{
	        	angular.forEach(options, function(value, key){
	        		this.push({name: value, supplied_value: ''});
	        	}, $scope.options);
        	}
        }
	}
	
	// method for executing a playcall against a player
	$scope.execute = function(){
		if(!$scope.canExecute) return alert('Please select a Player and Play Call first.');
		if($scope.isExecuting) return;
		
		$scope.isExecuting = true;
		
		var outputFunc = function(response) {
			$scope.isExecuting = false;
			$scope.playbookOutput = (response.data.output) ? 
					response.data.output : response.data;
		};
		
		// prepare options, we cannot use ng-repeat (key, value) + ng-model
		//  which would be more efficient: see http://jsfiddle.net/sirhc/z9cGm/
		var options = {};
		angular.forEach($scope.options, function(obj, key){
    		this[obj.name] = obj.supplied_value;
    	}, options);
		
		
		ExecutePlay.get({
			playerId: $scope.selectedPlayer,
			playcallId: $scope.selectedPlayCall,
			options: options
		})
		// promise.then(successCallback, errorCallback)
		.then(outputFunc, outputFunc);
		
	}
}

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
		
		$scope.options = [];
		if(type == 'PlayCall' && $scope[property])
		{
			$scope.options = options
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
		
		ExecutePlay.get({
			playerId: $scope.selectedPlayer,
			playcallId: $scope.selectedPlayCall,
		})
		// promise.then(successCallback, errorCallback)
		.then(outputFunc, outputFunc);
		
	}
}

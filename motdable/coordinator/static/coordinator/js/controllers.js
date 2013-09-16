'use strict';

/* Controllers */

function MainCtrl($scope, Players, PlayCalls) {
	// populate player list from django rest-framework
	Players.query(function(data){
		$scope.players = data;
		$scope.selectedPlayer = null;
	});
	
	PlayCalls.query(function(data){
		$scope.playcalls = data;
		$scope.selectedPlayCall = null;
	});
	
	// methods for toggling selection of current player/playcall
	$scope.selectItem = function(id, type){
		var property = 'selected' + type;
		$scope[property] = ($scope[property] == id) ? null : id;
		
		$scope.canExecute = ($scope.selectedPlayer && $scope.selectedPlayCall);
		console.log($scope.canExecute);
	}
}

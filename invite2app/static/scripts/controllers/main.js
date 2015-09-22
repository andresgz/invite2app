'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:MainController
 * @description
 * # MainController
 * Controller of the application
 * Handles information from the API to be connected with the view
 */
angular.module('frontApp')
  .controller('MainController',
    ['$scope', 'User', 'Friend', 'FriendInside', 
    function ($scope, User, Friend, FriendInside) {

    // Users of the application
    $scope.users = User.query();
    // List of name friends
    $scope.name_friends = [];
    // Chosen friends to send invite
    $scope.selected_friends = [];
    // My friends retrieved in the API
    $scope.friends = [];

    var next_page = null;
    var busy = false;
    var load_ended = false;
    $scope.loadFriends = function(){
        if (busy) return;
        if (load_ended) return;
        busy = true;
        var args = {};
        if (next_page != null) {
            args = {after: next_page};
        }
        var request = Friend.query(args, function(){
            if(request.data.length>0){
                $scope.friends = $scope.friends.concat(request.data);
                next_page = request.paging.cursors.after;
            }else{
                load_ended = true;
            }
            busy = false;
        });
    };

    $scope.resetFriends = function(){
        $scope.friends = [];
        next_page = null;
    };
    // Collects the names of People using the application
    var friends_inside = FriendInside.query(function(){
        for(var index in friends_inside){
            $scope.name_friends.push(friends_inside[index].name);
        }
    });

    // Executed when a friend is clicked
    $scope.update_invite_friends = function(friend, index){
        if($scope.friendInApp(friend.name)){
            bootbox.alert("This user is already using the App.");
            return;
        }
        var element_index = $scope.selected_friends.indexOf(friend.id);

        if($scope.selected_friends.indexOf(friend.id)<0){
            $scope.friends[index].active = true;
            $scope.selected_friends.push(friend.id);
        }else{
            $scope.friends[index].active = false;
            $scope.selected_friends.splice(element_index,1);
        }

        $scope.value_friends = $scope.selected_friends.join(',');

    }

    // Checks if the user is in the list of the invited friends
    $scope.friendInApp = function(friend_name){
        return $scope.name_friends.indexOf(friend_name)>-1 ? true : false;
    };

    // Uncheck the selected friends
    // @todo: There is a better way by updating just the selected elements
    $scope.resetSelectedFriends = function(){

        $scope.$apply(function() {
            for(var index in $scope.friends){
                $scope.friends[index].active = false;
            }
            $scope.selected_friends = [];
            $scope.value_friends = '';
        });
    };

    // Handles the validation of the Invite form
    $scope.submitForm = function(){
        $scope.entry = new FriendInside();
        $scope.entry.friends_ids = $scope.value_friends;

            if ($scope.inviteForm.$valid) {

                bootbox.confirm("You are about to invite "+$scope.selected_friends.length+" friends. Are you sure?", function(result) {
                    if(result){
                        FriendInside.save($scope.entry, function(data){ 
                            bootbox.alert("Yur invitation was sent succesfully!");

                        }, function(error){
                            bootbox.alert("There was an error. Please try again");
                        });
                        
                    }
                }); 
            }else{
                bootbox.alert("Please choose 1 or more fiends to invite!");
            }
    };

}]);

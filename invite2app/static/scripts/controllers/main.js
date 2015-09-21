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


    $scope.loadFriends = function(){
        var request = Friend.query(function(){
            $scope.friends = request.data;
        });
    };

    $scope.loadFriends();

    var friends_inside = FriendInside.query(function(){
        for(var index in friends_inside){
            $scope.name_friends.push(friends_inside[index].name);
        }

    });

    // Executed when a checkbox is triggered
    $scope.update_invite_friends = function(friend, index, invite_friend){
        if(invite_friend){
            $scope.selected_friends.push(friend.id);
        }else{
            var element_index = $scope.selected_friends.indexOf(friend.id);
            if(element_index > -1){
                $scope.selected_friends.splice(element_index,1);
            }
        }
        $scope.value_friends = $scope.selected_friends.join(',');

    }

    // Checks if the user is in the list of the invited friends
    $scope.friendInApp = function(friend_name){
        return $scope.name_friends.indexOf(friend_name)>-1 ? true : false;
    };

    // Handles the validation of the Invite form
    $scope.submitForm = function(){
        $scope.entry = new FriendInside();
        $scope.entry.friends_ids = $scope.value_friends;

            if ($scope.inviteForm.$valid) {
                    FriendInside.save($scope.entry, function(data){ 
                        bootbox.alert("Yur invitation was sent succesfully!");
                        $scope.loadFriends();

                    }, function(error){
                        bootbox.alert("There was an error. Please try again");
                    });
            }else{
                bootbox.alert("Please choose 1 or more fiends to invite!");
            }
    };

}]);

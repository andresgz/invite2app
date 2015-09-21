'use strict';

/**
 * @ngdoc service
 * @name frontApp.Friend
 * @description
 * # Service to query API with information about friends
 * Factory in the frontApp.
 */
angular.module('frontApp')
  .factory('Friend', 
    function($resource){
      return $resource('/api/friends/:id', {},{
        query: { method: 'GET', isArray:false},
      });
  });

angular.module('frontApp')
  .factory('FriendInside', 
    function($resource){
      return $resource('/api/friends_inside/:id', {},{
        query: { method: 'GET', isArray:true},
        save: {method:'POST', headers: {'X-CSRFToken' : csrf }}
      });
  });
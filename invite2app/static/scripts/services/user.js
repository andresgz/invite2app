'use strict';

/**
 * @ngdoc service
 * @name frontApp.Todo
 * @description
 * # Todo
 * Factory in the frontApp.
 */
angular.module('frontApp')
  .factory('User', 
    function($resource){
      return $resource('/api/users/:id', {},{
        query: { method: 'GET', isArray:true},
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
      });
  });
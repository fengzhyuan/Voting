function HomeService($resource) {
  var that = this;
  that.QRes = $resource(_urlPrefixes.API + "questions/:id");
  that.getQuestions = function(params) {
    return that.QRes.query(params).$promise;
  };
  that.updateChoice = function(id, vote) {
    var Choice = $resource(_urlPrefixes.API + "choices/:id", {id: '@id'});
    var choice = Choice.get({id: id}, function() {
      choice.votes = vote;
      choice.$save();
    });
  };
}
angular.module("Home")
  .service("HomeService", ["$resource", HomeService]);
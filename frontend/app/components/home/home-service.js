function HomeService($resource) {
  var that = this;
  that.HomeResource = $resource(_urlPrefixes.API + "questions/:question_id");
  that.getQuestions = function(params) {
    return that.HomeResource.query(params).$promise;
  };
}
angular.module("Home")
  .service("HomeService", ["$resource", HomeService]);
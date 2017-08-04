function StatController($http, $routeParams, $scope) {  
  var that = this;
  $scope.questionId = $routeParams.qid;
  $scope.labels = [];
  $scope.data = [];

  that.init = function () {
    $http.get(_urlPrefixes.API + "questions/"+$scope.questionId)
      .then(function(response) {
        var question = response.data;
        var choices = question.choices;

        for (var i = 0, l = choices.length; i < l; ++i) {
          choices[i] = JSON.parse(choices[i]);
          $scope.labels.push(choices[i].text);
          $scope.data.push(choices[i].vote);
        }
      });
  };
}

angular.module("Stat", ["chart.js"])
  .controller("StatController", [
    "$http",
    "$routeParams",
    "$scope",
    StatController
  ]);
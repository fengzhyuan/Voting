
function HomeController($http, $location) {  
  var that = this;
  
  that.question = [];
  that.choice = null;
  that.onchange = function (choice) {
    that.choice = choice;
  };
  that.onsubmit = function () {
    that.choice.vote += 1
    $http.put(_urlPrefixes.API + `choices/${that.choice.id}/`, 
    {
      id: that.choice.id, 
      votes: that.choice.vote,
      question: that.question.id,
      choice_text: that.choice.text
    })
      .then(function(data) {
        console.log(data);
        $location.path('/stat').search({qid: that.question.id});
      }, function(response) {
        console.log(JSON.stringify(response));
      });
  };
  that.init = function () {
    $http.get(_urlPrefixes.API + "questions/").then(function(data) {
      var questions = data.data;
      var indx = Math.floor(questions.length * Math.random());
      that.question = questions[indx];
      for (var i = 0, l = that.question.choices.length; i < l; ++i) {
        that.question.choices[i] = JSON.parse(that.question.choices[i]);
      }
    });
  };
}

angular.module("Home")  
  .controller("HomeController", [
    "$http",
    "$location",
    HomeController
  ]);

function HomeController(HomeService) {  
  var that = this;
  
  that.question = [];
  that.selectedIndex = -1;
  that.onchange = function (id) {
    that.selectedIndex = id; console.log(id);
    return false;
  };
  that.init = function () {
    return HomeService.getQuestions().then(function(data) {
      var indx = Math.floor(data.length * Math.random());
      that.question = data[indx];
      for (var i = 0, l = that.question.choices.length; i < l; ++i) {
        that.question.choices[i] = JSON.parse(that.question.choices[i]);
      }
    });
  };
}

angular.module("Home")  
  .controller("HomeController", [
    "HomeService",
    HomeController
  ]);
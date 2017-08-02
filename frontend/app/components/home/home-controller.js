function HomeController(HomeService) {  
  var that = this;
  
  that.question = null;
  that.init = function () {
    return HomeService.getQuestions().then(function(data) {
      that.question = data;
    });
  };
}

angular.module("Home")  
  .controller("HomeController", [
    "HomeService",
    HomeController
  ]);
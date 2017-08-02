
function StatController(StatService) {  
  var that = this;
  
  that.init = function () {
    return StatService.getVotes().then(function(data) {
    });
  };
}

angular.module("Stat")  
  .controller("StatController", [
    "StatService",
    StatController
  ]);
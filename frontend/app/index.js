require("angular/angular");
require("angular-route/angular-route");
require("angular-resource/angular-resource");
require("./components/home/home");
require("./components/stat/stat");
require("angular-ui-bootstrap");
var routesConfig = require("./routes");

_ = require("lodash");
_urlPrefixes = {
  API: "api/",
  TEMPLATES: "static/app/"
};

angular.module("myApp", [
  "Home",
  "Stat",
  "ngResource",
  "ngRoute",
  "ui.bootstrap",
]);

angular.module("myApp").config(routesConfig);